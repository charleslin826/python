#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Relay On Off

import time
import RPi.GPIO as GPIO

relay = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(relay, GPIO.OUT)

dly = 500
while True:
    try:
        GPIO.output(relay, GPIO.HIGH)
        print "High"
        time.sleep(dly / 1000.0)
        GPIO.output(relay, GPIO.LOW)
        print "Low"
        time.sleep(dly / 1000.0)
        dly -= 10
        if dly < 1:
            dly = 500
    except:
        GPIO.cleanup()
