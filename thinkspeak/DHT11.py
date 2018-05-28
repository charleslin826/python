#!/usr/bin/python

import sys
import urllib2
import RPi.GPIO as GPIO
import Adafruit_DHT
from time import sleep

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    # return dict
    return (str(RH), str(T))

    #use sys.argv if needed
if len(sys.argv) < 2:
    ('Usage: python http_get.py PRIVATE_KEY')
    exit(0)

print 'starting...'
baseUrl = 'https://api.thingspeak.com/update?api_key=%s' % sys.argv[1]
while Ture:
    RH, T = getSensorData()
    print T
    print RH
    f = urllib2.urlopen(baseUrl + "&field1="+RH+"field2="+T)
    print "HTTP Response: " + f.read()
    f.close()
    sleep(20)


