#!/usr/bin/python

import sys
import urllib2
import RPi.GPIO as GPIO
from time import sleep
from random import randint as ri
import Adafruit_DHT
import json

# import math

READ_API_KRY = "EKAV2U7DG3H6SSY4"
CHANNEL_ID = "485559"

RELAY_PIN = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(RELAY_PIN, GPIO.OUT)


# main() function     
def main():
    f = open('db_file', 'w+')
    while True:
        try:
            conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feed/last?api_key=%s"
                                   % (CHANNEL_ID, READ_API_KRY))
            response = conn.read()
            print "http status code= %s" % (conn.getcode())
            data = json.loads(response)
            # print data
            # for idx, feed in enumerate(data['feeds']):
            #print str(idx) + "      DH: " + feed['field1'] + ", T: " + feed['field2'] + ", GAS: " + feed['field3'] + ", Relay: " + feed['field4']
	    
            # print "End of Record"
            print data['field1'] 
            print data['field2']
            print data['field3']
            print data['field4']
            f.write(str(data))
            
            conn.close()
            sleep(1)
        except:
            f.close()
            print "\nExiting"
            break


# call main
if __name__ == '__main__':
    main()
