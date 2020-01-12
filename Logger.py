import sqlite3

database = 'auth.db'

def log(id, status):
    conn = sqlite3.connect(database)
    conn.execute("INSERT INTO logs(access_time, id, status) \
        VALUES(datetime('now', 'localtime'), ?, ?);", (id, status))
    conn.commit()
    conn.close()

def init():
    conn = sqlite3.connect(database)
    conn.execute('CREATE TABLE IF NOT EXISTS logs ( \
        access_time TEXT PRIMARY KEY, \
        id INTEGER NOT NULL, \
        status TEXT);')
    conn.commit()
    conn.close()

def main():
    init()
    print('Database initialized')

if __name__ == '__main__':
    main()
