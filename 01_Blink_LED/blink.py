import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print('using pin%d'%ledPin)

def destroy():
    GPIO.cleanup()
    print('cleaned up')

if __name__ == '__main__':
    setup()
    try:
        while True:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        destroy()