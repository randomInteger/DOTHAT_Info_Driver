#!/usr/bin/env python3
"""
This code is intended to produce data for display
on a 16x3 display such as the Pimrioni Display-o-Tron
hat (raspberry pi).

This code can be pulled into a script that controls
the Display-o-Tron.

This version is for python 3.3+, and is only intended
for raspbian/debian.

"""
import os
import re
import time
import json
import socket
import subprocess
import netifaces as ni
from netifaces import AF_INET, AF_INET6, AF_LINK
from time import strftime

class DotHatInfo:
    """
    A class that delivers data intended for a DOTHAT.

    All modules return a tuple of three strings that
    are meant to be written as lines 1,2,3 on a 16x3
    Display-o-Tron.
    """
    def __init__(self, param1="", param2=""):
        """
        Constructor
        """
        # try:
        #     (param1, param2)
        # except NameError:
        #     tprint("Attempt to initialize DotHatInfo class object failed due to missing arguments!  Exiting!")
        #     raise
        #Initialize object data
        self.hostname = "google.com"
        self.public_ip = "8.8.8.8"

    def time_date(self):
    """
    Returns a tuple of three strings for display.
    """
        #Get system time
        ymd = strftime("%Y-%m-%d")
        hms = strftime("%H:%M:%S")
        epoch = int(time.time())
        return (ymd, hms, epoch)

    def disk_info(self):
    """
    Returns a tuple of three strings for display.
    """
        #Get root partition free space
        df = subprocess.Popen(["df", "-h", "/"], stdout=subprocess.PIPE)
        output = df.communicate()[0]
        #Split the second line output into a tuple of strings
        #This is a bit of a hasty one-liner...
        (device, size, used, available, percent, mountpoint) = output.decode("utf-8").split("\n")[1].split()
        return ("Disk: " + mountpoint, "Free: " + percent, "Avail: " + available)

    def mem_info(self):
    """
    Returns a tuple of three strings for display.
    """
        #Get % free memory
        cmd_memfree = "free | grep Mem | awk \'{print $4/$2 * 100.0}\'"
        mem = subprocess.Popen(cmd_memfree, stdout=subprocess.PIPE, shell=True)
        output = mem.communicate()[0]
        percmemfree = "Free:  " + str(int(float(output.decode("utf-8")))) + '%'
        #get total allocated swap (should be zero if all is good)
        cmd_swaptotal = "free -m | grep Swap | awk \'{print $2}\'"
        mem = subprocess.Popen(cmd_swaptotal, stdout=subprocess.PIPE, shell=True)
        output = mem.communicate()[0]
        swaptotal = "Swap:  " + str(int(float(output.decode("utf-8")))) + 'MB'
        return ("Memory:", percmemfree, swaptotal)

    def network_ok(self):
    """
    Returns a tuple of three strings for display.
    """
        #Test system public DNS resolution
        try:
            socket.gethostbyname(self.hostname)
            dns = "DNS OK"
        except socket.gaierror as e:
            dns = "NO DNS"
        #Test for ping to 8.8.8.8 = can we ping the outside world.
        #response of 0 means success
        netcheck = os.system("ping -c 1 " + self.public_ip + " > /dev/null 2>&1")
        if netcheck == 0:
            internet = "INET OK"
        else:
            internet = "NO INET"
        return ("Network", dns, internet)

    def iface_info(self):
    """
    Returns a list of three-string tuples for display,
    since each interface will produce more than one screen
    of info (one for ip, one for netmask)
    """
        interfaces = []
        #Get interfaces via netifaces
        ifaces = ni.interfaces()
        #Iterate over the interfaces
        for iface in ifaces:
            #Populate IP and netmsk
            if AF_INET in ni.ifaddresses(iface).keys():
                inet = ni.ifaddresses(iface)[AF_INET]
                link = ni.ifaddresses(iface)[AF_LINK]
                if 'addr' in inet[0].keys():
                        ipv4address = inet[0]['addr']
                if 'netmask' in inet[0].keys():
                        netmask = inet[0]['netmask']
            elif AF_INET6 in ni.ifaddresses(iface).keys():
                inet = ni.ifaddresses(iface)[AF_INET6]
                link = ni.ifaddresses(iface)[AF_LINK]
                ipv4address = ipv4address = inet[0]['addr']
                netmask = inet[0]['netmask']
            else:
                ipv4address = "no ip"
                netmask = "n/a"

            #Append the address screen
            line1 = iface
            if len(ipv4address) < 17:
                line2 = ipv4address
                line3 = ''
            else:
                line2 = ipv4address[:16]
                line3 = ipv4address[16:32]
            interfaces.append((line1, line2, line3))

            #Append the netmask screen
            line1 = iface + " mask"
            if len(netmask) < 17:
                line2 = netmask
                line3 = ""
            else:
                line2 = netmask[:16]
                line3 = netmask[16:32]
            interfaces.append((line1, line2, line3))
        return interfaces
