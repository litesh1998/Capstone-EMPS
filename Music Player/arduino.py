import serial

ser= serial.Serial()
ser.port='COM3'
ser.baudrate=9600
ser.open()
while True:
    print("Waitng For Gesture")
    g=ser.readline()
    g=g.decode("utf-8").strip('\r\n')
    print(g)