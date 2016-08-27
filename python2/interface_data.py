#!/usr/bin/env python
"""
This code is intended to produce data for display
on a 16x3 display such as the Pimrioni Display-o-Tron
hat (raspberry pi).

This code can be pulled into a script that controls
the Display-o-Tron.

This version is for python 2.x

"""
import os
import time
import json
import socket
import subprocess
import netifaces as ni
from netifaces import AF_INET, AF_INET6, AF_LINK
from time import strftime

#Variables for testing dns and internet connectivity
hostname = "google.com"
public_ip = "8.8.8.8"

#Test system public DNS resolution
try:
    socket.gethostbyname('google.com')
    dns = True
except socket.gaierror as e:
    dns = False

#Test for ping to 8.8.8.8 = can we ping the outside world.
#response of 0 means success
internet = os.system("ping -c 1 " + public_ip + " > /dev/null 2>&1")

#Get interfaces via netifaces
ifaces = ni.interfaces()

#Get root partition free space
df = subprocess.Popen(["df", "-h", "/"], stdout=subprocess.PIPE)
output = df.communicate()[0]
#Split the second line output into a tuple of strings
(device, size, used, available, percent, mountpoint) = output.split("\n")[1].split()

#Get system time
ymd = strftime("%Y-%m-%d")
hms = strftime("%H:%M:%S")
epoch = int(time.time())

#Start the sample dispay output
print "****************"
#Time and date info
print ymd
print hms
print epoch
print "****************"
#Disk info
print "Disk: ", mountpoint
print "Used: ", percent
print "Free: ", available
print "****************"
#Network info
print "Network:"
if internet == 0:
    print "Internet OK"
else:
    print "No Internet"

if dns:
    print "DNS OK"
else:
    print "No DNS"
print "****************"
#Iterate over the interfaces
for iface in ifaces:
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
    print "****************"
    #Interface address
    print iface
    if len(ipv4address) < 17:
        print ipv4address
    else:
        print ipv4address[:16]
        print ipv4address[16:32]
    print "****************"
    #Interface netmask
    print iface,"mask"
    if len(netmask) < 17:
        print netmask
    else:
        print netmask[:16]
        print netmask[16:32]
print "****************"
