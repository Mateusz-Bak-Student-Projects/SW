import RFIDScanner as rfid
import Authentication as auth
import PrimaryPass as pass0
import SecondaryPass as pass1
import SafeLock as lock
import Logger as logger
import Display

def authenticate(retries=1):
    id = rfid.scan_RFID()
    if id == None:
        return id, False, 'RFID failed'
    if auth.is_admin(id):
        return None, True, 'Admin mode enabled'
    if not auth.is_valid(id):
        return id, False, 'User not registered'
    Display.write(' PIN 1: ', 'Enter passcode')
    for i in range(retries):
        primary = pass0.read()
        if auth.verify(id, primary, 0):
            break
        elif i + 1 == retries:
            return id, False, 'Primary password incorrect'
        Display.write(' PIN 1: Invalid', 'Enter passcode')
    Display.write(' PIN 1: ********', ' PIN 2: ')
    for i in range(retries):
        secondary = pass1.read()
        if auth.verify(id, secondary, 1):
            break
        elif i + 1 == retries:
            return id, False, 'Secondary password incorrect'
        Display.write(' PIN 1: ********', ' PIN 2: Invalid')
    return id, True, 'Access granted'

def access(id):
    lock_id = auth.get_lock(id)
    lock.open(lock_id)
    while(lock.is_open(lock_id)):
        scan = rfid.scan_RFID(block=False)
        if scan == id:
            reset_password(id)
    lock.close(lock_id)

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
                Display.write('Unlocked')
                access(id)
        elif valid:
            Display.write('Locked', 'Admin mode')
            admin_mode()
        Display.write('Locked')

if __name__ == '__main__':
    main()
