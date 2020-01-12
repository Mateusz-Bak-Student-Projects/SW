# import Adafruit_BBIO.GPIO as GPIO
# import time

# trigger = 'P9_16'
# echo = 'P9_41'

# def read_distance():
#    GPIO.output(trigger, True)
#    time.sleep(0.00001)
#    GPIO.output(trigger, False)
#    while GPIO.input(echo) == 0:
#        pulseStart = time.time()
#    while GPIO.input(echo) == 1:
#        pulseEnd = time.time()
#    pulseDuration = pulseEnd - pulseStart
#    distance = pulseDuration * 17150
#    distance = round(distance, 2)
#    return distance

# def init():
#     GPIO.setup(trigger, GPIO.OUT)
#     GPIO.setup(echo, GPIO.IN)

def read():
    return input('PIN 2: ')
