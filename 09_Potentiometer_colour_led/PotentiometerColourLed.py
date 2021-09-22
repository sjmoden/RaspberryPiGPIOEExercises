import RPi.GPIO as GPIO
import time
import random
from ADCDevice import *

redPin = 11
greenPin = 13
bluePin = 15
adc = ADCDevice()

def setup():
    global pwmRed,pwmGreen,pwmBlue, adc
    
    if(adc.detectI2C(0x4b)):
            adc = ADS7830()
            
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup([redPin, greenPin, bluePin], GPIO.OUT)
    GPIO.output([redPin, greenPin, bluePin], GPIO.HIGH)

    pwmRed = GPIO.PWM(redPin, 500)
    pwmRed.start(0)
    
    pwmGreen = GPIO.PWM(greenPin, 500)
    pwmGreen.start(0)
    
    pwmBlue = GPIO.PWM(bluePin, 500)
    pwmBlue.start(0)

def setColour(r_val,g_val,b_val):
    pwmRed.ChangeDutyCycle(max(r_val,0))
    pwmGreen.ChangeDutyCycle(max(g_val,0))
    pwmBlue.ChangeDutyCycle(max(b_val,0))
    print ('r=%d, g=%d, b=%d ' %(r_val ,g_val, b_val))
    
def getColourValue(chn):
    value = adc.analogRead(chn)
    calculatedValue = (value-1)* 100  / 254.0
    return max(calculatedValue,0)

def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    adc.close()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        while True:
            setColour(getColourValue(0),getColourValue(1),getColourValue(2))
            time.sleep(0.03)
    finally:
        destroy()
