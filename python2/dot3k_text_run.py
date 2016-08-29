#!/usr/bin/env python
"""
Write three lines to the screen, update once every 2 seconds.

Currently just prints to the terminal, will be updated later
with working DOTHAT code.

Python 2 version
"""
#import dothat.lcd as lcd
import sys
import time
import signal
from InterfaceData import DotHatInfo

#shutdown message
message="V2FyYmVycnkgUGkgU2NhbiBUb29sIDEuMA=="

#Define an explicit signal handler
#intent is to use this to catch SIGINT
def signal_handler(signal, frame):
    print 'INFO: SIGINT/Ctrl+C received! Killing dot3k_text.py!'
    #End the program with a static message
    # lcd.set_cursor_position(0, 0)
    # lcd.write(message[:16])
    # lcd.set_cursor_position(0, 1)
    # lcd.write(message[16:32])
    # lcd.set_cursor_position(0, 2)
    # lcd.write(message[32:])
    sys.exit(0)

#def write_screen(line1, line2, line3):
    # lcd.set_cursor_position(0, 0)
    # lcd.write(line1)
    # lcd.set_cursor_position(0, 1)
    # lcd.write(line2)
    # lcd.set_cursor_position(0, 2)
    # lcd.write(line3)

def fake_write_screen(line1, line2, line3):
    print "****************"
    print line1
    print line2
    print line3
    print "****************"

#Start the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

#Create the data source object
dot3kdata = DotHatInfo()

#Start driving text to the board
while True:

    #Grab a three line tuple of time/data data and print
    (line1, line2, line3) = dot3kdata.time_date()
    #write_screen(line1, line2, line3)
    fake_write_screen(line1, line2, line3)
    time.sleep(2)

    #Grab a three line tuple of disk data and print
    (line1, line2, line3) = dot3kdata.disk_info()
    #write_screen(line1, line2, line3)
    fake_write_screen(line1, line2, line3)
    time.sleep(2)

    #Grab a three line tuple of mem data and print
    (line1, line2, line3) = dot3kdata.mem_info()
    #write_screen(line1, line2, line3)
    fake_write_screen(line1, line2, line3)
    time.sleep(2)

    #Grab a three line tuple of network data and print
    (line1, line2, line3) = dot3kdata.network_ok()
    #write_screen(line1, line2, line3)
    fake_write_screen(line1, line2, line3)
    time.sleep(2)

    #Get a list of three-line tuples containing interface
    #data and print them all
    ifaces_screens = dot3kdata.iface_info()
    for iface in ifaces_screens:
        #write_screen(iface[0], iface[1], iface[2])
        fake_write_screen(iface[0], iface[1], iface[2])
        time.sleep(2)
