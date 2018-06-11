#!/usr/bin/python 
#coding=utf-8
#  讀取MQ2氣體偵測數值
#舊的錯的import spidev #使用SPI通訊協定(和I2C UART一樣都是通訊協定) 
import time 
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


#spi = spidev.SpiDev() 
#spi.open(0, 0) 
#count =0 

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        print "wrong port num"
        return -1
    r = spi.xfer2([1, 8 + adcnum<< 4, 0])
    adcount = ((r[1] & 3) << 8) + r[2]
    return adcount 

while True:
    #tmp1 = int(round(readadc(0) / 1.024)) 
    #tmp2 = int(round(readadc(1) / 1.024)) 
    #tmp3 = int(round(readadc(2) / 1.024))
    tmp4 = int(round(mcp.read_adc(3) / 1.024)) # MQ2 in port 3
    print "Gas value = ", tmp4
    #count = count + 1
    time.sleep(1)
