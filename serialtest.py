import serial

device="/dev/ttyACM0"

ser=serial.Serial(device,9600)

while True:
	print ser.readline()