import RPi.GPIO as GPIO
import time
import typing
import requests
import json

dataPin = 18
latchPin = 16
clockPin = 12
digitPin = (11,13,15,19) 

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
    def displayJ(self):
        self.outputPins(False,False,False,False,True,True,True,False)
    def displayMLeft(self):
        self.outputPins(False,False,True,True,False,True,True,True)
    def displayMRight(self):
        self.outputPins(False,False,True,True,False,True,True,True)
    def displayR(self):
        self.outputPins(False,False,True,True,False,False,False,True)
    def displayCharacter(self, character: str):
        if len(character)>1:
            raise Exception("Must be a single character")
        
        upperCharacter = character.upper()
        if upperCharacter == 'J':
            self.displayJ()
        elif upperCharacter == 'E':
            self.displayE()
        elif upperCharacter == 'S':
            self.displayFive()
        elif upperCharacter == 'A':
            self.displayA()
        elif upperCharacter == 'M':
            self.displayMLeft()    
        elif upperCharacter == 'R':
            self.displayR()    
        elif upperCharacter == '!':
            self.displayMRight()
        elif upperCharacter == '0':
            self.displayZero()
        elif upperCharacter == '1':
            self.displayOne()
        elif upperCharacter == '2':
            self.displayTwo()
        elif upperCharacter == '3':
            self.displayThree()
        elif upperCharacter == '4':
            self.displayFour()
        elif upperCharacter == '5':
            self.displayFive()
        elif upperCharacter == '6':
            self.displaySix()
        elif upperCharacter == '7':
            self.displaySeven()
        elif upperCharacter == '8':
            self.displayEight()
        elif upperCharacter == '9':
            self.displayNine()
        else:
            self.displayNothing()

def OutPutToFourCharacterDisplay(chip: Chip74HC595, input: str, secondsToDisplay: int):
    input = input.replace('M','M!').replace('m','M!')
    if len(input)>4:
        raise Exception('Input must be equal to or less than 4 characters')
    
    endTime = time.time() + secondsToDisplay
    while time.time() < endTime:
        intervalTime = 0.003
        paddedInput = input.rjust(4,' ')
        chip.displayNothing()
        GPIO.output(digitPin[0],GPIO.LOW)
        GPIO.output(digitPin[1],GPIO.HIGH)
        GPIO.output(digitPin[2],GPIO.HIGH)
        GPIO.output(digitPin[3],GPIO.HIGH)
        chip.displayCharacter(paddedInput[-4])
        time.sleep(intervalTime)
        GPIO.output(digitPin[0],GPIO.HIGH)
        GPIO.output(digitPin[1],GPIO.LOW)
        GPIO.output(digitPin[2],GPIO.HIGH)
        GPIO.output(digitPin[3],GPIO.HIGH)
        chip.displayCharacter(paddedInput[-3])
        time.sleep(intervalTime)
        GPIO.output(digitPin[0],GPIO.HIGH)
        GPIO.output(digitPin[1],GPIO.HIGH)
        GPIO.output(digitPin[2],GPIO.LOW)
        GPIO.output(digitPin[3],GPIO.HIGH)
        chip.displayCharacter(paddedInput[-2])
        time.sleep(intervalTime)
        GPIO.output(digitPin[0],GPIO.HIGH)
        GPIO.output(digitPin[1],GPIO.HIGH)
        GPIO.output(digitPin[2],GPIO.HIGH)
        GPIO.output(digitPin[3],GPIO.LOW)
        chip.displayCharacter(paddedInput[-1])
        time.sleep(intervalTime)

class PlayerDetails(object):
    def __init__(self, name, rank, score):
        self.Name = name
        self.Score = score
        self.Rank = rank
    
class FantasyFootballApi(object):
    uri = "https://fantasy.premierleague.com/api/leagues-classic/873285/standings/"
    def __init__(self):
        self.Players = []
        
    def PopulateLeagueDetails(self):
        try:
            response = requests.get("https://fantasy.premierleague.com/api/leagues-classic/873285/standings/")
            for entry in response.json()['standings']['results']:
                player = PlayerDetails(entry['player_name'],entry['rank'],entry['total'])
                self.Players.append(player)
        except:
            pass        

chip = Chip74HC595(dataPin,latchPin,clockPin) 

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    for pin in digitPin:
        GPIO.setup(pin,GPIO.OUT)
        
    try:
        
        GPIO.output(digitPin[0],GPIO.HIGH)
        GPIO.output(digitPin[1],GPIO.HIGH)
        GPIO.output(digitPin[2],GPIO.HIGH)
        GPIO.output(digitPin[3],GPIO.HIGH)
        while True:
            api = FantasyFootballApi()
            api.PopulateLeagueDetails()
            timeToDisplay = 3
            
            minutesToDisplay = 5
            endTime = time.time() + minutesToDisplay * 60
            while time.time() < endTime:
                if len(api.Players) == 0:
                    OutPutToFourCharacterDisplay(chip,'err',timeToDisplay)
                    
                for player in api.Players:
                    if 'jess' in player.Name.lower():
                        OutPutToFourCharacterDisplay(chip,'jess',timeToDisplay)
                    elif 'sam' in player.Name.lower():
                        OutPutToFourCharacterDisplay(chip,'sam',timeToDisplay)
                    OutPutToFourCharacterDisplay(chip,str(player.Rank),timeToDisplay)
                    OutPutToFourCharacterDisplay(chip,str(player.Score),timeToDisplay)
                
    finally:
        GPIO.cleanup()