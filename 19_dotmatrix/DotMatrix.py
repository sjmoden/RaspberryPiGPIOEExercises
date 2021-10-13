import RPi.GPIO as GPIO
import time

class DotMatrix(object):
    def __init__(self, dataPin, latchPin, clockPin):
        self.dataPin = dataPin
        self.latchPin = latchPin
        self.clockPin = clockPin

    blank = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    zero = [0x00, 0x00, 0x3E, 0x41, 0x41, 0x3E, 0x00, 0x00]
    one = [0x00, 0x00, 0x21, 0x7F, 0x01, 0x00, 0x00, 0x00]
    two = [0x00, 0x00, 0x23, 0x45, 0x49, 0x31, 0x00, 0x00]
    three = [0x00, 0x00, 0x22, 0x49, 0x49, 0x36, 0x00, 0x00]
    four = [0x00, 0x00, 0x0E, 0x32, 0x7F, 0x02, 0x00, 0x00]
    five = [0x00, 0x00, 0x79, 0x49, 0x49, 0x46, 0x00, 0x00]
    six = [0x00, 0x00, 0x3E, 0x49, 0x49, 0x26, 0x00, 0x00]
    seven = [0x00, 0x00, 0x60, 0x47, 0x48, 0x70, 0x00, 0x00]
    eight = [0x00, 0x00, 0x36, 0x49, 0x49, 0x36, 0x00, 0x00]
    nine = [0x00, 0x00, 0x32, 0x49, 0x49, 0x3E, 0x00, 0x00]
    letterA = [0x00, 0x00, 0x3F, 0x44, 0x44, 0x3F, 0x00, 0x00]
    letterB = [0x00, 0x00, 0x7F, 0x49, 0x49, 0x36, 0x00, 0x00]
    letterC = [0x00, 0x00, 0x3E, 0x41, 0x41, 0x22, 0x00, 0x00]
    letterD = [0x00, 0x00, 0x7F, 0x41, 0x41, 0x3E, 0x00, 0x00]
    letterE = [0x00, 0x00, 0x7F, 0x49, 0x49, 0x41, 0x00, 0x00]
    letterF = [0x00, 0x00, 0x7F, 0x48, 0x48, 0x40, 0x00, 0x00]
    letterG = [0x00, 0x1C, 0x22, 0x41, 0x41, 0x45, 0x06, 0x00]
    letterH = [0x00, 0x7F, 0x08, 0x08, 0x08, 0x08, 0x7f, 0x00]
    letterI = [0x00, 0x7F, 0x08, 0x08, 0x08, 0x08, 0x7f, 0x00]
    letterI = [0x00, 0x41, 0x41, 0x7F, 0x41, 0x41, 0x00, 0x00]
    letterJ = [0x00, 0x06, 0x01, 0x41, 0x41, 0x7F, 0x40, 0x40]
    letterK = [0x00, 0x00, 0x7F, 0x08, 0x14, 0x22, 0x41, 0x40]
    letterL = [0x00, 0x7F, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00]
    letterM = [0x00, 0x7F, 0x20, 0x10, 0x10, 0x20, 0x7F, 0x00]
    letterN = [0x00, 0x7F, 0x10, 0x08, 0x04, 0x02, 0x7F, 0x00]
    letterO = [0x00, 0x00, 0x3E, 0x41, 0x41, 0x3E, 0x00, 0x00]
    letterP = [0x00, 0x3F, 0x48, 0x48, 0x48, 0x30, 0x00, 0x00]
    letterQ = [0x00, 0x3E, 0x41, 0x41, 0x45, 0x3E, 0x01, 0x00]
    letterR = [0x00, 0x3F, 0x4C, 0x4A, 0x49, 0x30, 0x00, 0x00]
    letterS = [0x00, 0x00, 0x79, 0x49, 0x49, 0x46, 0x00, 0x00]
    letterT = [0x00, 0x40, 0x40, 0x7F, 0x40, 0x40, 0x00, 0x00]
    letterU = [0x00, 0x7E, 0x01, 0x01, 0x01, 0x7E, 0x00, 0x00]
    letterV = [0x00, 0x7C, 0x02, 0x01, 0x01, 0x02, 0x7c, 0x00]
    letterW = [0x00, 0x7F, 0x02, 0x04, 0x04, 0x02, 0x7F, 0x00]
    letterX = [0x00, 0x41, 0x22, 0x14, 0x08, 0x14, 0x22, 0x41]
    letterY = [0x40, 0x20, 0x10, 0x0F, 0x10, 0x20, 0x40, 0x00]
    letterZ = [0x00, 0x43, 0x45, 0x49, 0x51, 0x61, 0x00, 0x00]
        
    def displayStaticImage(self, imageArray):
        if len(imageArray) != 8:
            raise Exception("Image must contain exactly 8 inputs")
        for colIndex in range(0,8):
            GPIO.output(self.latchPin,GPIO.LOW)
            for row in range(8,-1,-1):
                GPIO.output(self.clockPin,GPIO.LOW)
                GPIO.output(self.dataPin,GPIO.HIGH if (0x01&(imageArray[colIndex]>>row)==0x01) else GPIO.LOW)
                GPIO.output(self.clockPin,GPIO.HIGH)
            for column in range(0,8):
                GPIO.output(self.clockPin,GPIO.LOW)
                GPIO.output(self.dataPin,GPIO.LOW if colIndex == column else GPIO.HIGH)
                GPIO.output(self.clockPin,GPIO.HIGH)
            GPIO.output(self.latchPin,GPIO.HIGH)
            time.sleep(0.001)

    def getInputFromChar(self, inputChar):
        inputCharToCheck = str(inputChar).upper()
        
        if inputCharToCheck == "A":
            return self.letterA
        if inputCharToCheck == "B":
            return self.letterB
        if inputCharToCheck == "C":
            return self.letterC
        if inputCharToCheck == "D":
            return self.letterD
        if inputCharToCheck == "E":
            return self.letterE
        if inputCharToCheck == "F":
            return self.letterF
        if inputCharToCheck == "G":
            return self.letterG
        if inputCharToCheck == "H":
            return self.letterH
        if inputCharToCheck == "I":
            return self.letterI
        if inputCharToCheck == "J":
            return self.letterJ
        if inputCharToCheck == "K":
            return self.letterJ
        if inputCharToCheck == "L":
            return self.letterL
        if inputCharToCheck == "M":
            return self.letterM
        if inputCharToCheck == "N":
            return self.letterN
        if inputCharToCheck == "O":
            return self.letterO
        if inputCharToCheck == "P":
            return self.letterP
        if inputCharToCheck == "Q":
            return self.letterQ
        if inputCharToCheck == "R":
            return self.letterR
        if inputCharToCheck == "S":
            return self.letterS
        if inputCharToCheck == "T":
            return self.letterT
        if inputCharToCheck == "U":
            return self.letterU
        if inputCharToCheck == "V":
            return self.letterV
        if inputCharToCheck == "W":
            return self.letterW
        if inputCharToCheck == "X":
            return self.letterX
        if inputCharToCheck == "Y":
            return self.letterY
        if inputCharToCheck == "Z":
            return self.letterZ
        if inputCharToCheck == "0":
            return self.zero
        if inputCharToCheck == "1":
            return self.one
        if inputCharToCheck == "2":
            return self.two
        if inputCharToCheck == "3":
            return self.three
        if inputCharToCheck == "4":
            return self.four
        if inputCharToCheck == "5":
            return self.five
        if inputCharToCheck == "6":
            return self.six
        if inputCharToCheck == "7":
            return self.seven
        if inputCharToCheck == "8":
            return self.eight
        if inputCharToCheck == "9":
            return self.nine
        if inputCharToCheck == " ":
            return self.blank
        raise Exception(f"Input Char must be a single character: {inputCharToCheck}")

    def createInputFromString(self, inputStr):
        message = []
        message += self.blank
        for char in inputStr:
            characterHex = self.getInputFromChar(char)
            for characterHexEntry in characterHex:
                if characterHexEntry != 0x00 or characterHex == self.blank:
                    message.append(characterHexEntry)
            message.append(0x00)
        return message
    
    def displayScrollingMessage(self, inputStr):
        message = self.createInputFromString(inputStr)
        posn = 0
        message += message
        lenArray = int(len(message)/2)
        while True:
            for i in range(0,20):
                self.displayStaticImage(message[posn:posn+8])
            posn = (posn + 1) % lenArray