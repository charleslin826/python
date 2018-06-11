#!/usr/bin/python

from Tkinter import *
import Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

relay = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(relay, GPIO.OUT)


def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    # return dict
    return (str(RH), str(T))


def relayOn():
    GPIO.output(relay, GPIO.HIGH)
    print "On"


def relayOff():
    GPIO.output(relay, GPIO.LOW)
    print "Off"


def update_chart(H, T):
    coord = 0, 0, 100, 100
    arcH = cavHT.create_arc(coord, start=0, extent=H, fill="red")
    coord = 100, 0, 200, 100
    arcT = cavHT.create_arc(coord, start=0, extent=T, fill="yellow")


def update_info():
    RH, T = getSensorData()
    msg = "Humidity: %s\nTemperature: %s" % (RH, T)
    print msg
    var.set(msg)
    update_chart(RH, T)
    # pnlMain.update_idletasks()
    pnlMain.after(1000, update_info)


pnlMain = PanedWindow(orient=VERTICAL)
pnlMain.pack(fill=BOTH, expand=1)

pnlRelay = PanedWindow(pnlMain)
pnlMain.add(pnlRelay)

btnRelayOn = Button(pnlRelay, text="On ", command=relayOn)
btnRelayOff = Button(pnlRelay, text="Off", command=relayOff)
varRelayControl = StringVar()
varRelayControl.set("Relay Control: ")
lblEmpty = Label(pnlRelay, textvariable=varRelayControl)

pnlRelay.add(lblEmpty)
pnlRelay.add(btnRelayOn)
pnlRelay.add(btnRelayOff)

pnlHT = PanedWindow(pnlMain)
pnlMain.add(pnlHT)

var = StringVar()
label = Label(pnlHT, textvariable=var, relief=RAISED)
label.config(font=("Courier", 20))

RH, T = getSensorData()
msg = "Humidity: %s\nTemperature: %s" % (RH, T)
var.set(msg)
pnlHT.add(label)

cavHT = Canvas(pnlHT, bg="blue", height=100, width=200)
update_chart(RH, T)
pnlHT.add(cavHT)

pnlMain.mainloop()
