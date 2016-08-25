#!/usr/bin/env python3

import os
import netifaces as ni
from netifaces import AF_INET, AF_LINK

hostname = "google.com"
public_ip = "8.8.8.8"
dns = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
internet = os.system("ping -c 1 " + public_ip + " > /dev/null 2>&1")

print("\nRegular terminal formatting:")

#List the interfaces
print("\nListing all interfaces:")
ifaces = ni.interfaces()
print(ifaces)

#Iterate over the interface list and print data
for iface in ifaces:
    ipv4address = ni.ifaddresses(iface)[AF_INET][0]['addr']
    netmask = ni.ifaddresses(iface)[AF_INET][0]['netmask']
    link = ni.ifaddresses(iface)[AF_LINK]
    inet = ni.ifaddresses(iface)[AF_INET]
    print("\nInterface %s has ip address %s" % (iface,ipv4address))
    print("%s LINK data:" % iface)
    print(link)
    print("%s INET data:" % iface)
    print(inet)

print("\nFormatting for 16x2 display")
print("************************************")
#response == 0 means ping succeeded
if internet == 0:
    print("Internet OK\n")
else:
    print("No Internet\n")
print("************************************")
#response == 0 means ping succeeded
if dns == 0:
    print("DNS OK\n")
else:
    print("No DNS\n")
for iface in ifaces:
    ipv4address = ni.ifaddresses(iface)[AF_INET][0]['addr']
    netmask = ni.ifaddresses(iface)[AF_INET][0]['netmask']
    link = ni.ifaddresses(iface)[AF_LINK]
    inet = ni.ifaddresses(iface)[AF_INET]
    print("************************************")
    print(iface,"ip")
    print(ipv4address)
    print("************************************")
    print(iface,"mask")
    print(netmask)
print("************************************")
