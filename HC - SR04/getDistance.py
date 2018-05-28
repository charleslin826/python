#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 讀取SONAR距離的數值 
import RPi.GPIO as GPIO
import time

TRIG_PIN = 13
ECHO_PIN = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# GPIO.output(TRIG_PIN, False)
# print "Waiting for sensor to settle"
# time.sleep(2)
# 
# GPIO.output(TRIG_PIN, True)
# time.sleep(0.00001)
# GPIO.output(TRIG_PIN, False)
# 
# while GPIO.input(ECHO_PIN) == 0:
#     pulse_start = time.time()
# 
# while GPIO.input(ECHO_PIN) == 1:
#     pulse_end = time.time()
# 
# pulse_duration = pulse_end-pulse_start
# 
# distance = pulse_duration * 17150
# 
# distance = round(distance, 2)
# 
# print "Distance: ", distance, " cm"

def getDistance():
    GPIO.output(TRIG_PIN, False)
    print "Waiting for sensor to settle"
    time.sleep(2)
    
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    
    return distance

while True:
    print "Distance: ", getDistance(), " cm"
    time.sleep(1)
    
GPIO.cleanup()