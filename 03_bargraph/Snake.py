import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPins, GPIO.OUT)
    GPIO.output(ledPins, GPIO.HIGH)

def loop():
    while True:
        for ledPin in ledPins:
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.5)
            
        for ledPin in ledPins:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.5)

def destroy():
    GPIO.cleanup()
    print('cleaned up')

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
