import RPi.GPIO as GPIO
import time

motorPins = (12, 16, 18, 22) 

def switchOnPin(posn):
    if posn > 3:
        raise Exception("Position not recognised")
    
    for pin in motorPins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.output(motorPins[posn], GPIO.HIGH)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    for pin in motorPins:
        GPIO.setup(pin,GPIO.OUT)
    
    try:
        waitTime = 0.003
        while True:
            time.sleep(1)
            for i in range(512):
                switchOnPin(0)
                time.sleep(waitTime)
                switchOnPin(1)
                time.sleep(waitTime)
                switchOnPin(2)
                time.sleep(waitTime)
                switchOnPin(3)
                time.sleep(waitTime)
            time.sleep(1)
            for i in range(512):
                switchOnPin(3)
                time.sleep(waitTime)
                switchOnPin(2)
                time.sleep(waitTime)
                switchOnPin(1)
                time.sleep(waitTime)
                switchOnPin(0)
                time.sleep(waitTime)
    finally:
        GPIO.cleanup()