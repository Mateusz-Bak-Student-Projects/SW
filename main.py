import RFIDScanner as rfid
import Authentication as auth
import PrimaryPass as pass0
import SecondaryPass as pass1
import SafeLock as lock
import Logger as logger
import Display
import time

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
    Display.write('Unlocked')
    lock_id = auth.get_lock(id)
    lock.open(lock_id)
    while(lock.is_open(lock_id)):
        scan = rfid.scan_RFID(block=False)
        if scan == id:
            if reset_password(id):
                Display.write('Unlocked', 'Passcode set')
            else:
                Display.write('Unlocked', 'Invalid passcode')
    lock.close(lock_id)

def admin_mode():
    Display.write('Locked', 'Admin mode')
    id = rfid.scan_RFID()
    if id == None:
        return
    if not auth.is_admin(id):
        if reset_password(id):
            Display.write('Locked', 'Passcode set')
        else:
            Display.write('Locked', 'Invalid passcode')
        time.sleep(3)

def reset_password(id, confirm=True):
    Display.write('+PIN 1: ', 'Set new passcode')
    primary = pass0.read(prompt='+PIN 1: ')
    Display.write(' PIN 1: ', 'Confirm passcode')
    if primary == None or (confirm and primary != pass0.read()):
        return False
    Display.write(' PIN 1: ********', '+PIN 2: ')
    secondary = pass1.read(prompt='+PIN 2: ')
    Display.write(' PIN 1: ********', ' PIN 2: Confirm')
    if secondary == None or (confirm and secondary != pass1.read()):
        return False
    auth.set(id, primary, secondary)
    return True

def main():
    while True:
        Display.write('Locked')
        id, valid, status = authenticate()
        print(status)
        if id != None:
            logger.log(id, status)
            if valid:
                access(id)
        elif valid:
            admin_mode()

if __name__ == '__main__':
    main()
