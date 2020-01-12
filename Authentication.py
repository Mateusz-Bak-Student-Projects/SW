import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--admin', help='grant or revoke admin priviledges to/from a specified id')
    args = parser.parse_args()

import sqlite3
import hashlib
import binascii
import os

database = 'auth.db'

def set(id, primary, secondary):
    primary = hash_password(primary)
    secondary = hash_password(secondary)
    conn = sqlite3.connect(database)
    conn.execute('INSERT INTO users(id, pass0, pass1) VALUES(?, ?, ?) \
        ON CONFLICT(id) DO UPDATE SET pass0=excluded.pass0, pass1=excluded.pass1;',
        (id, primary, secondary))
    conn.commit()
    conn.close()

def verify(id, password, level):
    column = ['pass0', 'pass1'][level]
    conn = sqlite3.connect(database)
    cursor = conn.execute('SELECT {} FROM users WHERE id=?;'.format(column), (id,))
    row = cursor.fetchone()
    conn.close()
    if row == None:
        return False
    return verify_password(password, row[0])

def is_valid(id):
    conn = sqlite3.connect(database)
    cursor = conn.execute('SELECT id FROM users WHERE id=?;', (id,))
    row = cursor.fetchone()
    conn.close()
    return row != None

def is_admin(id):
    conn = sqlite3.connect(database)
    cursor = conn.execute('SELECT id FROM admins WHERE id=?;', (id,))
    row = cursor.fetchone()
    conn.close()
    return row != None

def get_lock(id):
    conn = sqlite3.connect(database)
    cursor = conn.execute('SELECT lock_id FROM users WHERE id=?;', (id,))
    row = cursor.fetchone()
    conn.close()
    return row[0]

def set_admin(id, value=True):
    conn = sqlite3.connect(database)
    if value:
        conn.execute('INSERT INTO admins(id) VALUES(?);', (id,))
    else:
        conn.execute('DELETE FROM admins WHERE id=?;', (id,))
    conn.commit()
    conn.close()
 
def hash_password(password):
    salt = hashlib.sha256(os.urandom(64)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(password, hashed):
    salt = hashed[:64].encode('ascii')
    correct = hashed[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == correct

def init():
    conn = sqlite3.connect(database)
    conn.execute('CREATE TABLE IF NOT EXISTS users ( \
        id INTEGER PRIMARY KEY, \
        pass0 TEXT NOT NULL, \
        pass1 TEXT NOT NULL, \
        lock_id INTEGER DEFAULT 0);')
    conn.execute('CREATE TABLE IF NOT EXISTS admins ( \
        id INTEGER PRIMARY KEY);')
    conn.commit()
    conn.close()

def main():
    global args
    id = args.admin
    if id is None:
        init()
        print('Database initialized')
    else:
        if is_admin(id):
            set_admin(id, False)
            print('Admin priviledges revoked from '+id)
        else:
            set_admin(id, True)
            print('Admin priviledges granted to '+id)

if __name__ == '__main__':
    main()
