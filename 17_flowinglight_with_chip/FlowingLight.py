import RPi.GPIO as GPIO
import time
import typing

dataPin = 11
latchPin = 13
clockPin = 15

class Chip74HC595(object):
    def __init__(self, dataPin, latchPin, clockPin):
        self.dataPin = dataPin
        self.latchPin = latchPin
        self.clockPin = clockPin
        
    def outputPins(self, output0: bool, output1: bool, output2: bool, output3: bool, output4: bool, output5: bool, output6: bool, output7: bool):
        for i in range(0,8):
            GPIO.output(latchPin,GPIO.LOW)
            for j in range(0,8):
                GPIO.output(clockPin,GPIO.LOW)
                GPIO.output(dataPin,
                            GPIO.HIGH
                            if (j == 0 and output0)
                            or (j == 1 and output1)
                            or (j == 2 and output2)
                            or (j == 3 and output3)
                            or (j == 4 and output4)
                            or (j == 5 and output5)
                            or (j == 6 and output6)
                            or (j == 7 and output7)
                            else GPIO.LOW)
                GPIO.output(clockPin,GPIO.HIGH)
            GPIO.output(latchPin,GPIO.HIGH)
    
chip = Chip74HC595(dataPin,latchPin,clockPin) 

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    
    try:
        while True:
            chip.outputPins(True,False,False,False,False,False,False,False)
            time.sleep(1)
            chip.outputPins(True,True,False,False,False,False,False,False)
            time.sleep(1)
            chip.outputPins(True,True,True,False,False,False,False,False)
            time.sleep(1)
            chip.outputPins(True,True,True,True,False,False,False,False)
            time.sleep(1)
            chip.outputPins(True,True,True,True,True,False,False,False)
            time.sleep(1)
            chip.outputPins(True,True,True,True,True,True,False,False)
            time.sleep(1)
            chip.outputPins(True,True,True,True,True,True,True,False)
            time.sleep(1)
            chip.outputPins(True,True,True,True,True,True,True,True)
            time.sleep(1)
    finally:
        GPIO.cleanup()