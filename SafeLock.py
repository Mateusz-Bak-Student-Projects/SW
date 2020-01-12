import Display
# import Adafruit_BBIO.PWM as PWM

# servo = 'P9_14'
locked = { 0 : False }

# def set_angle(angle):
#     dutyCycle = 0.05 * angle + 3
#     PWM.set_duty_cycle(servo, dutyCycle)

# def init():
#     PWM.start(servo, 3, 50)

def open(id):
    # set_angle(90)
    locked[id] = False
    Display.write('Unlocked\n\r')

def close(id):
    # set_angle(0)
    locked[id] = True
    Display.write('Locked\n\r')

def is_open(id):
    return not locked[id]
