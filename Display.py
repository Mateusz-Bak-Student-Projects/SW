# import Adafruit_BBIO.UART as UART
# import serial

# def write(*lines):
#     text = '\r' + '\n'.join(lines)
#     UART.setup("UART1")
#     ser = serial.Serial(port="/dev/ttyO1", baudrate=9600)
#     ser.close()
#     ser.open()
#     ser.write(text.encode('utf-8'))
#     ser.close()

def write(*lines):
    for line in lines:
        print(line)
