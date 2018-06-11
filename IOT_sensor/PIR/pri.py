#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 讀取HC SR501 的數值 
import RPi.GPIO as GPIO
import time

PIR_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)

while True:
    print (GPIO.input(PIR_PIN))
    time.sleep(0.5)





