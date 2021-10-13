import RPi.GPIO as GPIO
from DotMatrix import *
    
dataPin   = 11
latchPin  = 13
clockPin = 15
    
if __name__ == '__main__':  # Program entrance
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    try:
        dotMatrix = DotMatrix(dataPin, latchPin, clockPin)
        while True:
            dotMatrix.displayScrollingMessage("Hello World")
        

    finally:
        GPIO.cleanup()  


