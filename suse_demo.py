import serial.tools.list_ports
import sys
import atexit
import platform
import RPi._GPIO as GPIO

def findArduinoUnoPort():
    portList = list(serial.tools.list_ports.comports())
    for port in portList:
        if "VID:PID=2341:0043" in port[0]\
            or "VID:PID=2341:0043" in port[1]\
            or "VID:PID=2341:0043" in port[2]:
            print(port)
            print(port[0])
            print(port[1])
            print(port[2])

            #please note: it is not sure [0]
            #returned port[] is no particular order
            #so, may be [1], [2]
            return port[0]

def doAtExit():
    if serialUno.isOpen():
        serialUno.close()
        print("Close serial")
        print("serialUno.isOpen() = " + str(serialUno.isOpen()))

def setupp():
	GPIO.setmode(GPIO.BOARD)
 
	# Setup GPIO Pins
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(32, GPIO.OUT)
	GPIO.setup(33, GPIO.OUT)
	GPIO.setup(35, GPIO.OUT)
 

if __name__ == '__main__':
	print("=== Auto scan for Arduino Uno connected port===")
	print("")
	print(platform.system(), platform.release())
	print(platform.dist())
	print("Python version " + platform.python_version())
	print("")
	atexit.register(doAtExit)

	unoPort = findArduinoUnoPort()
	if not unoPort:
	    print("No Arduino Uno found")
	    sys.exit("No Arduino Uno found - Exit")

	print("Arduino Uno found: " + unoPort)
	print()

	serialUno = serial.Serial(unoPort, 9600)
	print("serialUno.isOpen() = " + str(serialUno.isOpen()))
	try:
		pwm12 = GPIO.PWM(12, 0.5)
		pwm32 = GPIO.PWM(32, 0.75)
		pwm33 = GPIO.PWM(33, 0.66)
		pwm35 = GPIO.PWM(35, 0.87)
		pwm12.start(0)
		pwm32.start(0)
		pwm33.start(0)
		pwm35.start(0)


		while True:
		    while (serialUno.inWaiting()==0):
		        pass
		    valueRead = serialUno.readline(500)
		    print(valueRead)
		    dutyCycle=(100*valueRead)/1023
		    pwm12.ChangeDutyCycle(dutyCycle)
		    pwm32.ChangeDutyCycle(dutyCycle)
		    pwm33.ChangeDutyCycle(dutyCycle)
		    pwm35.ChangeDutyCycle(dutyCycle)

	except KeyboardInterrupt:
		pwm12.stop()
		pwm32.stop()
		pwm33.stop()
		pwm35.stop()
        GPIO.cleanup()