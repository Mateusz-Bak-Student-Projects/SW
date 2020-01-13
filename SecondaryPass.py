import numpy as np
from bisect import bisect
# import Adafruit_BBIO.GPIO as GPIO
# import time

# triggerPins = ['P9_16']
# echoPins = ['P9_41']

# def read_value(index):
#    trigger = triggerPins[index]
#    echo = echoPins[index]
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
#     for trigger, echo in zip(triggerPins, echoPins):
#         GPIO.setup(trigger, GPIO.OUT)
#         GPIO.setup(echo, GPIO.IN)

# def read():
#     passcodeLength = 8
#     nSegments = 4
#     maxValue = 40
#     bounds = np.linspace(0, maxValue, num=(nSegments+1))
#     nInputs = len(triggerPins)
#     restart = True
#     while restart:
#         for i in range(nInputs):
#             v = read_value(i)
#             state = bisect(bounds[1:], v)
#             if state < nSegments:
#                 break
#             if i == nInputs - 1:
#                 restart = False
#     states = np.full(nInputs, nSegments)
#     passcode = ''
#     while len(passcode) < passcodeLength:
#         for i, state in enumerate(states):
#             v = read_value(i)
#             newState = states[i] = bisect(bounds[1:], v)
#             if state == nSegments and newState < nSegments:
#                 passcode += hex(i * nSegments + newState)[2]
#     return passcode

def read():
    return input('PIN 2: ')
