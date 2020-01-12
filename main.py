import RFIDScanner as rfid
import Authentication as auth
import PrimaryPass as pass0
import SecondaryPass as pass1
import SafeLock as lock
import Logger as logger

def authenticate():
    id = rfid.scan_RFID()
    if id == None:
        return id, False, 'RFID failed'
    if auth.is_admin(id):
        return None, True, 'Admin mode enabled'
    if not auth.is_valid(id):
        return id, False, 'User not registered'
    primary = pass0.read()
    if not auth.verify(id, primary, 0):
        return id, False, 'Primary password incorrect'
    secondary = pass1.read()
    if not auth.verify(id, secondary, 1):
        return id, False, 'Secondary password incorrect'
    return id, True, 'Access granted'

def access(id):
    lock_id = auth.get_lock(id)
    lock.open(lock_id)
    while(lock.is_open()):
        scan = rfid.scan_RFID(block=False)
        if scan == id:
            reset_password(id)
    lock.close()

def admin_mode():
    id = rfid.scan_RFID()
    if id == None:
        return
    if not auth.is_admin(id):
        reset_password(id)

def reset_password(id):
    primary = pass0.read()
    if primary == None:
        return
    secondary = pass1.read()
    if secondary == None:
        return
    auth.set(id, primary, secondary)

def main():
    while True:
        id, valid, status = authenticate()
        print(status)
        if id != None:
            logger.log(id, status)
            if valid:
                access(id)
        elif valid:
            admin_mode()
            print('Admin mode disabled')

if __name__ == '__main__':
    main()
