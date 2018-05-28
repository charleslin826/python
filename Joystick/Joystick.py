#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 讀取 Joystick 的數值 
import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
count = 0


def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        print "wrong port num"
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcount = ((r[1] & 3) << 8) + r[2]
    return adcount


while True:
    tmp1 = int(round(readadc(0) / 1.024))  # SW
    tmp2 = int(round(readadc(1) / 1.024))  # VRY
    tmp3 = int(round(readadc(2) / 1.024))  # VRX
    # print "SW:", tmp1
    # print "Y:", tmp2
    # print "X:", tmp3
    if tmp1 == 0 and tmp2 > 400:
        print "press"
	print tmp1
    if tmp2 == 0:
        print "right"
    if tmp2 > 600:
        print "left"
    if tmp3 < 5:
        print "up"
    if tmp3 > 600:
        print "down"
    count = count + 1
    time.sleep(1)
