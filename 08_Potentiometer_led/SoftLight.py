import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledPin = 11
adc = ADCDevice()

if __name__ == '__main__':
    try:
        if(adc.detectI2C(0x4b)):
            adc = ADS7830()
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ledPin,GPIO.OUT)
        p = GPIO.PWM(ledPin,1000)
        p.start(0)
        
        while True:
            value = adc.analogRead(0)
            calculatedValue = (value-1) / 254.0
            p.ChangeDutyCycle(calculatedValue)
            voltage = calculatedValue * 3.3
            print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
            time.sleep(0.03)
            
    finally:
        p.stop()
        GPIO.cleanup()
        adc.close()