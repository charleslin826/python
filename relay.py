
import sys
import urllib
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(38, GPIO.OUT)

while True:
    try:
        GPIO.output(38, True)
        print "hight"
        time.sleep(5)
        print "low"
        GPIO.output(38, False)
        time.sleep(5)
    except:
        GPIO.cleanup()
