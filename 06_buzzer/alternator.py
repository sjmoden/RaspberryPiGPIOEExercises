import RPi.GPIO as GPIO
import time 
import math

buzzerPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT) 
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print('Start')
    setup()
    try:
        p = GPIO.PWM(buzzerPin, 1)
        p.start(0);
        
        while True:
            if GPIO.input(buttonPin)==GPIO.LOW:
                print('On')
                p.start(50)
                for x in (0,361):
                    sinVal = math.sin(x * (math.pi / 180.0))
                    toneVal = 2000 + sinVal * 500
                    p.ChangeFrequency(toneVal)
                    time.sleep(.01)
            else:
                print('Off')
                p.stop()
    except KeyboardInterrupt:
        destroy()
    finally:
        p.stop()

