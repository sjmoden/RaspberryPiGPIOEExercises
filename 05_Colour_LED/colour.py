import RPi.GPIO as GPIO
import time
import random

redPin = 11
greenPin = 12
bluePin = 13

def setup():
    global pwmRed,pwmGreen,pwmBlue
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
    pwmRed.ChangeDutyCycle(r_val)
    pwmGreen.ChangeDutyCycle(g_val)
    pwmBlue.ChangeDutyCycle(b_val)
    print ('r=%d, g=%d, b=%d ' %(r_val ,g_val, b_val))
    
def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        while True:
            rand=random.randint(0,100)
            for r_val in range(0, 100, 1):
                setColour(r_val,rand,rand)
                time.sleep(.1)
            for g_val  in range(0, 100, 1):
                setColour(rand,g_val,rand)
                time.sleep(.1)
            for b_val  in range(0, 100, 1):
                setColour(rand,rand,b_val)
                time.sleep(.1)
    except KeyboardInterrupt:
        destroy()