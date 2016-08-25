# python_iface_inspector
Simple example python code to inspect interfaces, format output example intended for 16x2 LED Raspberry PI display.

This is just an example of how you might quickly scoop up interface data so that you can rotate messages on a raspberry pi 16x2 LCD display (adafruit).  That code is not shown, but there is an excellent guide here:  https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/usage

Installation:

I recommend you always sandbox python projects in a virtualenv.  The requirements.txt file is intended for this use.

Example:

"virtualenv -p /usr/bin/python3.4 ./.env"
"source .env/bin/activate"
"pip install -r ./requirements.txt"

Then just run the script from the source folder:

./interface_data.py

Example output (Please view this in raw mode, markup doesn't like the formatting)
$ ./interface_data.py

Regular terminal formatting:

Listing all interfaces:
['lo', 'eth0', 'eth1']

Interface lo has ip address 127.0.0.1
lo LINK data:
[{'addr': '00:00:00:00:00:00', 'peer': '00:00:00:00:00:00'}]
lo INET data:
[{'addr': '127.0.0.1', 'netmask': '255.0.0.0', 'peer': '127.0.0.1'}]

Interface eth0 has ip address 172.16.0.247
eth0 LINK data:
[{'addr': '00:50:56:b0:92:3b', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
eth0 INET data:
[{'addr': '172.16.0.247', 'netmask': '255.255.0.0', 'broadcast': '172.16.255.255'}]

Interface eth1 has ip address 10.5.60.247
eth1 LINK data:
[{'addr': '00:50:56:b0:3a:76', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
eth1 INET data:
[{'addr': '10.5.60.247', 'netmask': '255.255.0.0', 'broadcast': '10.5.255.255'}]

Formatting for 16x2 display
- - - - - - - - - - - - - 
Internet OK

- - - - - - - - - - - - - 
DNS OK

- - - - - - - - - - - - - 
lo ip
127.0.0.1
- - - - - - - - - - - - - 
lo mask
255.0.0.0
- - - - - - - - - - - - - 
eth0 ip
172.16.0.247
- - - - - - - - - - - - - 
eth0 mask
255.255.0.0
- - - - - - - - - - - - - 
eth1 ip
10.5.60.247
- - - - - - - - - - - - - 
eth1 mask
255.255.0.0
- - - - - - - - - - - - - 
