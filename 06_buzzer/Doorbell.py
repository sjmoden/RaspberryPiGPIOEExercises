import RPi.GPIO as GPIO

buzzerPin = 11
buttonPin = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(buzzerPin, GPIO.OUT) 
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	print('Start')
	setup()
	try:
		while True:
			if GPIO.input(buttonPin)==GPIO.LOW:
				GPIO.output(buzzerPin,GPIO.HIGH) 
				print('On')
			else:
				GPIO.output(buzzerPin,GPIO.LOW) 
				print('Off')
	except KeyboardInterrupt:
		destroy()
