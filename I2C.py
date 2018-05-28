#!/usr/bin/python
#coding=utf-8
#BH1750FVI

import smbus
import time

DEVICE = 0x23 

POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07

CONTINUOUS_HIGH_RES_MODE_1 = 0x10
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
CONTINUOUS_LOW_RES_MODE_1 = 0x23

ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21
ONE_TIME_LOW_RES_MODE_1 = 0x23

bus = smbus.SMBus(1)

def convertToNumber(data):
    return((data[1] + (256 * data[0])) / 1.2)
def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
#    print data
    return convertToNumber(data)

def main():
    while True:
        print "Light Level : " + str(readLight()) + " lx"
        time.sleep(0.5)

if __name__=="__main__":
    main()
        




