#!/usr/bin/env python
"""
Display-o-Tron hat driver using threading to drive the lights 
and text on different update frequencies.  Text data from InterfaceData.py.

Adapted from the example code at https://github.com/pimoroni/dot3k

This version incorporates python threading to run both
the lights update loop and the text update loop independently.

Commented code is as yet, untested.

"""
import sys
import time
import signal
import threading
#import dothat.lcd as lcd
from InterfaceData import DotHatInfo

#Define an explicit signal handler
#intent is to use this to catch SIGINT
def signal_handler(signal, frame):
    """
    dothat code is currently block commented.
    print statement to show updates in testing.
    """
    print('INFO: SIGINT/Ctrl+C received! Cleaning up.')
    #End the program with a static message
    # lcd.set_cursor_position(0, 0)
    # lcd.write(message[:16])
    # lcd.set_cursor_position(0, 1)
    # lcd.write(message[16:32])
    # lcd.set_cursor_position(0, 2)
    # lcd.write(message[32:])

    #slowly dim the 18 backlights (6 x (r+g+b)) on the way out
    # for i in range(19):
    #     backlight.set(i,30)  #0-255
    #     time.sleep(0.3)
    # #slowly raise and then drop the bargraph leds
    # for i in range(6):
    #     time.sleep(0.5)
    #     backlight.graph_set_led_state(led, 1)
    # for i in range(6):
    #     time.sleep(0.5)
    #     backlight.graph_set_led_state(led, 0)
    sys.exit(0)

def _write_screen(line1, line2, line3):
    """
    This is untested until my dothat arrives.
    """
    lcd.set_cursor_position(0, 0)
    lcd.write(line1)
    lcd.set_cursor_position(0, 1)
    lcd.write(line2)
    lcd.set_cursor_position(0, 2)
    lcd.write(line3)

def _fake_write_screen(line1, line2, line3):
    """
    Temp replacement for _write_screen.
    """
    print("****************")
    print(line1)
    print(line2)
    print(line3)
    print("****************")

def run_lights():
    """
    dothat code is currently block commented.
    print statement to show updates in testing.
    """
    # #initialize loop counter.
    # x = 0
    while True:
        # x += 3
        # x %= 360
        print("run_lights_update")
        # #Set the backlight brightness for the 6 leds x 3 colors each
        # #brightness is 0-255
        # for i in range(19):
        #     backlight.set(i,255)
        #
        # #Set the backlight 6 led gradient, which we will update
        # #as x goes from 3 to 360 in increments of 3 (120 steps)
        # backlight.sweep((360.0 - x) / 360.0)
        #
        # #Set the bar graph led which will oscillate slowly up and down
        # backlight.set_graph(abs(math.sin(x / 100.0)))
        #
        # #led loop update rate
        time.sleep(0.1)


def run_text():
    """
    dothat code is currently block commented.
    print statement to show updates in testing.
    """
    #Create the data source object
    dot3kdata = DotHatInfo()
    while True:

        #Grab a three line tuple of time/data data and print
        (line1, line2, line3) = dot3kdata.time_date()
        #_write_screen(line1, line2, line3)
        _fake_write_screen(line1, line2, line3)
        time.sleep(2)

        #Grab a three line tuple of disk data and print
        (line1, line2, line3) = dot3kdata.disk_info()
        #_write_screen(line1, line2, line3)
        _fake_write_screen(line1, line2, line3)
        time.sleep(2)

        #Grab a three line tuple of mem data and print
        (line1, line2, line3) = dot3kdata.mem_info()
        #_write_screen(line1, line2, line3)
        _fake_write_screen(line1, line2, line3)
        time.sleep(2)

        #Grab a three line tuple of network data and print
        (line1, line2, line3) = dot3kdata.network_ok()
        #_write_screen(line1, line2, line3)
        _fake_write_screen(line1, line2, line3)
        time.sleep(2)

        #Get a list of three-line tuples containing interface
        #data and print(them all
        ifaces_screens = dot3kdata.iface_info()
        for iface in ifaces_screens:
            #_write_screen(iface[0], iface[1], iface[2])
            _fake_write_screen(iface[0], iface[1], iface[2])
            time.sleep(2)

#Start the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

#Drive the dothat
lights = threading.Thread(target=run_lights,args=())
text = threading.Thread(target=run_text,args=())
lights.start()
text.start()
