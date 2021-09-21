import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPins, GPIO.OUT)
    GPIO.output(ledPins, GPIO.HIGH)

def loop():
    alternator = True
    while True:
        i =0
        if alternator:
            i =0
        else:
            i =1
        
        for ledPin in ledPins:
            if i % 2 == 0:
                GPIO.output(ledPin, GPIO.LOW)
            else:
                GPIO.output(ledPin, GPIO.HIGH)
            
            i+=1
        alternator = not alternator
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