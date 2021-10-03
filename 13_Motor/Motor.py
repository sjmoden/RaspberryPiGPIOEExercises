import RPi.GPIO as GPIO
import time
from ADCDevice import *

adc = ADCDevice()
upperBackwardValue = 123
lowerForwardValue = 132
motoRPin1 = 13
motoRPin2 = 11
enablePin = 15

if __name__ == '__main__':
    try:
        if(adc.detectI2C(0x4b)):
            adc = ADS7830()
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(motoRPin1,GPIO.OUT)
        GPIO.setup(motoRPin2,GPIO.OUT)
        GPIO.setup(enablePin,GPIO.OUT)
        
        p = GPIO.PWM(enablePin,1000)
        p.start(0)
        
        while True:
            value = adc.analogRead(0)
            if value <= upperBackwardValue:
                direction = 'forward'
                GPIO.output(motoRPin1,GPIO.HIGH)
                GPIO.output(motoRPin2,GPIO.LOW)
                print((upperBackwardValue - value)*100/upperBackwardValue)
                p.ChangeDutyCycle((upperBackwardValue - value)*100/upperBackwardValue)
            elif value >= lowerForwardValue:
                direction = 'backward'
                GPIO.output(motoRPin1,GPIO.LOW)
                GPIO.output(motoRPin2,GPIO.HIGH)
                print((value - lowerForwardValue)*100/(255-lowerForwardValue))
                p.ChangeDutyCycle((value - lowerForwardValue)*100/(255-lowerForwardValue))
            else:
                direction = 'stopped'
                GPIO.output(motoRPin1,GPIO.LOW)
                GPIO.output(motoRPin2,GPIO.LOW)
                p.ChangeDutyCycle(0)
            
            print ('ADC Value : %d, Direction: %s'%(value,direction))
            time.sleep(0.1)
            
    finally:
        p.stop()
        GPIO.cleanup()
        adc.close()