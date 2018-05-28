#!/usr/bin/python

import sys
import urllib2
import RPi.GPIO as GPIO
import Adafruit_DHT
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import smbus

DEVICE = 0x23

POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07
ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1)
def convertToNumber(data):
    return((data[1] + (256 * data[0])) / 1.2)
def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
    return convertToNumber(data)



# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
     


def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    # return dict
    return (str(RH), str(T))

    #use sys.argv if needed
if len(sys.argv) < 2:
    print('Usage: python http_get.py PRIVATE_KEY')
    exit(0)

print 'starting...'
baseUrl = 'https://api.thingspeak.com/update?api_key=%s' % sys.argv[1]
while True:
    RH, T = getSensorData()
    print T
    print RH
    values = str(mcp.read_adc(3))
    print values
    print "Light Level : " + str(readLight()) + " lx"
    f = urllib2.urlopen(baseUrl + "&field1="+RH+"&field2="+T+"&field3="+values+"&field4="+str(readLight()))
    print "HTTP Response: " + f.read()
    f.close()
    sleep(5)


