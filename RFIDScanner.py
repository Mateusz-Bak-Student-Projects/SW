# import Adafruit_BBIO.UART as UART
# import serial

# def scan_RFID(block=True):
#     timeout = None if block else 0
#     UART.setup("UART1")
#     with serial.Serial(port="/dev/ttyO1", baudrate=9600, timeout=timeout) as ser:
#         b = ser.read_until('\n')
#         if len(b) == 0:
#             return None
#         else:
#             ser.timeout = None
#             s = b.decode('utf-8')
#             while s[-1] != '\n':
#                 b = ser.read_until('\n')
#                 if len(b) == 0:
#                     return None
#                 s.append(b.decode('utf-8'))
#             return int(s[:-1])

def scan_RFID(block=True):
    return int(input())
