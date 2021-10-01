import RPi.GPIO as GPIO
import time
import math
from ADCDevice import *

def ConvertCelciusToKelvin(celcius):
    return 273.15 + celcius

def ConvertKelvinToCelcius(kelvin):
    return kelvin - 273.15

firstResistorResistance = 10000
inputVoltage = 3.3
thermalIndex = 3950
temperature1 = ConvertCelciusToKelvin(25) 
adc = ADCDevice()

#Voltage Dividor
#Resistance of the thermometer can be calculated using the equeation below.
#https://www.seeedstudio.com/blog/2019/10/09/voltage-dividers-everything-you-need-to-know/#:~:text=%20Voltage%20Divider%20Circuit%20%201%20R1%20%3D,divided%20voltage%20%281%2F4%20of%20input%20voltage%29%20More%20

def GetSecondResistorResistance(outputVoltage):
    return (firstResistorResistance * outputVoltage) / (inputVoltage - outputVoltage)

#We will be using this formula to calculate the Temperature
#T2 = 1/(1/T1 + ln(Rt/R)/B)

def GetTemperature(outputVoltage):
    celciusValue = 1/( (1/temperature1) + (math.log(GetSecondResistorResistance(outputVoltage)/firstResistorResistance)/thermalIndex) )
    return ConvertKelvinToCelcius(celciusValue)

def GetVoltage(reading):
    calculatedValue = reading / 255.0
    return calculatedValue * 3.3

if __name__ == '__main__':
    try:
        if(adc.detectI2C(0x4b)):
            adc = ADS7830()
        
        while True:
            value = adc.analogRead(0)
            voltage = GetVoltage(value)
            temperature = GetTemperature(voltage)
            
            print ('ADC Value : %d, Voltage : %.2f, Temperature: %.2f'%(value,voltage, temperature))
            time.sleep(1)
            
    finally:
        adc.close()