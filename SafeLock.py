# import Adafruit_BBIO.PWM as PWM
# import Adafruit_BBIO.GPIO as GPIO

# servo = 'P9_14'
# button = 'P8_12'
locked = { 0 : False }

# def set_angle(angle):
#     dutyCycle = 0.05 * angle + 3
#     PWM.set_duty_cycle(servo, dutyCycle)

# def get_button():
#     return GPIO.input(button) == 1

# def init():
#     PWM.start(servo, 3, 50)
#     GPIO.setup(button, GPIO.IN)

def open(id):
    # set_angle(90)
    locked[id] = False

def close(id):
    # set_angle(0)
    locked[id] = True

def is_open(id):
    # return not get_button()
    return not locked[id]
