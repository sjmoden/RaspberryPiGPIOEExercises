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
        
    def outputPins(self, outputDecimalPoint: bool, outputMiddleBar: bool, outputTopLeft: bool, outputBottomLeft: bool, outputBottomBar: bool, outputBottomRight: bool, outputTopRight: bool, outputTopBar: bool):
        for i in range(0,8):
            GPIO.output(latchPin,GPIO.LOW)
            for j in range(0,8):
                GPIO.output(clockPin,GPIO.LOW)
                GPIO.output(dataPin,
                            GPIO.LOW
                            if (j == 0 and outputDecimalPoint)
                            or (j == 1 and outputMiddleBar)
                            or (j == 2 and outputTopLeft)
                            or (j == 3 and outputBottomLeft)
                            or (j == 4 and outputBottomBar)
                            or (j == 5 and outputBottomRight)
                            or (j == 6 and outputTopRight)
                            or (j == 7 and outputTopBar)
                            else GPIO.HIGH)
                GPIO.output(clockPin,GPIO.HIGH)
            GPIO.output(latchPin,GPIO.HIGH)
    def displayNothing(self):
        self.outputPins(False,False,False,False,False,False,False,False)
    def displayZero(self):
        self.outputPins(False,False,True,True,True,True,True,True)
    def displayOne(self):
        self.outputPins(False,False,False,False,False,True,True,False)
    def displayTwo(self):
        self.outputPins(False,True,False,True,True,False,True,True)
    def displayThree(self):
        self.outputPins(False,True,False,False,True,True,True,True)
    def displayFour(self):
        self.outputPins(False,True,True,False,False,True,True,False)
    def displayFive(self):
        self.outputPins(False,True,True,False,True,True,False,True)
    def displaySix(self):
        self.outputPins(False,True,True,True,True,True,False,True)
    def displaySeven(self):
        self.outputPins(False,False,False,False,False,True,True,True)
    def displayEight(self):
        self.outputPins(False,True,True,True,True,True,True,True)
    def displayNine(self):
        self.outputPins(False,True,True,False,True,True,True,True)
    def displayA(self):
        self.outputPins(False,True,True,True,False,True,True,True)
    def displayB(self):
        self.outputPins(False,True,True,True,True,True,False,False)
    def displayC(self):
        self.outputPins(False,False,True,True,True,False,False,True)
    def displayD(self):
        self.outputPins(False,True,False,True,True,True,True,False)
    def displayE(self):
        self.outputPins(False,True,True,True,True,False,False,True)
    def displayF(self):
        self.outputPins(False,True,True,True,False,False,False,True)
    
chip = Chip74HC595(dataPin,latchPin,clockPin) 

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    try:
        sleepInterval = 0.5
        while True:
            chip.displayNothing()
            time.sleep(sleepInterval)
            chip.displayZero()
            time.sleep(sleepInterval)
            chip.displayOne()
            time.sleep(sleepInterval)
            chip.displayTwo()
            time.sleep(sleepInterval)
            chip.displayThree()
            time.sleep(sleepInterval)
            chip.displayFour()
            time.sleep(sleepInterval)
            chip.displayFive()
            time.sleep(sleepInterval)
            chip.displaySix()
            time.sleep(sleepInterval)
            chip.displaySeven()
            time.sleep(sleepInterval)
            chip.displayEight()
            time.sleep(sleepInterval)
            chip.displayNine()
            time.sleep(sleepInterval)
            chip.displayA()
            time.sleep(sleepInterval)
            chip.displayB()
            time.sleep(sleepInterval)
            chip.displayC()
            time.sleep(sleepInterval)
            chip.displayD()
            time.sleep(sleepInterval)
            chip.displayE()
            time.sleep(sleepInterval)
            chip.displayF()
            time.sleep(sleepInterval)
    finally:
        GPIO.cleanup()