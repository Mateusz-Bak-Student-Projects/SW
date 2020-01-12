import Display
# import Adafruit_BBIO.PWM as PWM

# servo = "P9_14"
open = False

# def set_angle(angle):
#     dutyCycle = 0.05 * angle + 3
#     PWM.set_duty_cycle(servo, dutyCycle)

# def init():
#     PWM.start(servo, 3, 50)

def open():
    # set_angle(90)
    open = True
    Display.write('Unlocked\n\r')

def close():
    # set_angle(0)
    open = False
    Display.write('Locked\n\r')

def is_open():
    return open
