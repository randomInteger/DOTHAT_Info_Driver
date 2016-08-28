# python_iface_inspector
Simple example python code to inspect interfaces, format output example intended for 16x3 Raspberry PI display such as the Pimoroni Display-o-Tron Hat.

For info on driving the DOT hat:
https://github.com/pimoroni/dot3k

Installation:

I recommend you always sandbox python projects in a virtualenv.  The requirements.txt file is intended for this use.

Example (Python3.4 version):

"virtualenv -p /usr/bin/python3.4 ./.env"
"source .env/bin/activate"
"pip install -r ./requirements.txt"

Then just run the script from the source folder:

./interface_data.py

Example output (Please view this in raw mode, markup doesn't like the formatting)
$ ./interface_data.py

- - - - - - - - - - - - - 
2016-08-27

23:45:29

1472341529
- - - - - - - - - - - - - 
Disk:  /

Used:  46%

Free:  4.1G
- - - - - - - - - - - - - 
Network:

Internet OK

DNS OK
- - - - - - - - - - - - - 
lo

127.0.0.1
- - - - - - - - - - - - - 
lo mask

255.0.0.0
- - - - - - - - - - - - - 
eth0

172.31.24.72
- - - - - - - - - - - - - 
eth0 mask

255.255.240.0
- - - - - - - - - - - - - 
docker0

172.17.0.1
- - - - - - - - - - - - - 
docker0 mask

255.255.0.0
- - - - - - - - - - - - - 
vethb29860a

fe80::f0b3:eaff:

fe5c:9b3a%vethb2
- - - - - - - - - - - - - 
vethb29860a mask

ffff:ffff:ffff:f

fff::/64
- - - - - - - - - - - - - 
