# python_iface_inspector
Simple example python code to inspect interfaces (as well as some other bonus data) and format the output. Intended as a template for data shown on a 16x3 Raspberry PI display such as the Pimoroni Display-o-Tron Hat.

Tested on debian linux.

My long term goal here is to pop the DOTHAT on my Warberry Pi build (https://github.com/secgroundzero/warberry) so that I have a box I can plug headless into a network and dump all of the network data.  Using a hat like this will make it trivial to learn the PI's dhcp address as well as confirm that the pi has network connectivity, without needing to hook up a monitor or SSH into the pi from another machine.  

For info on driving the DOT hat:
https://github.com/pimoroni/dot3k

Installation:

I recommend you always sandbox python projects in a virtualenv.  The requirements.txt file is intended for this use.

Example (Python3.4 version):

virtualenv -p /usr/bin/python3.4 ./.env

source .env/bin/activate

pip install -r ./requirements.txt

Then just run the script from the source folder:

./interface_data.py

This is just way of showing how you might grab and format this data, to run it on the DOTHAT you would adapt their example scripts to loop over the strings in the print statements in this script.  I will upload that version, with screenshots as soon as I get my DOTHAT and get it all tied together.

Example output:
[![solarized dualmode](https://github.com/randomInteger/python_iface_inspector/blob/master/Screen%20Shot%202016-08-27%20at%205.13.02%20PM.png)]
