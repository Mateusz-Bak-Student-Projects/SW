import numpy as np
# import Adafruit_BBIO.ADC as ADC

# analog = 'P9_33'

# def read_value():
#     return ADC.read(analog) * 1.8

# def init():
#     ADC.setup()

# def read():
#     passcodeLength = 8
#     nSegments = 16
#     maxValue = 5
#     delta = maxValue / nSegments * 0.25
#     # 0 |-(--)-|-(--)-|-(--)-|-(--)-| maxValue
#     bounds = np.linspace(0, maxValue, num=(nSegments+1))
#     lb = (bounds + delta)[:-1]
#     ub = (bounds - delta)[1:]
#     while read_value() > ub[0]:
#         pass
#     state = 0
#     direction = 1
#     passcode = ''
#     while len(passcode) < passcodeLength:
#         v = read_value()
#         if state < nSegments - 1 and v > lb[state+1]:
#             if direction < 0:
#                 passcode += hex(state)[2]
#             state += 1
#             direction = 1
#         elif state > 0 and v < ub[state-1]:
#             if direction > 0:
#                 passcode += hex(state)[2]
#             state -= 1
#             direction = -1
#     return passcode

def read():
    return input('PIN 1: ')
