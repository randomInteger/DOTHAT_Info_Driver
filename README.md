# DOTHAT_Info_Driver:  A class for scraping system data, and the code to run it on a Pimoroni Display-o-Tron Raspberry PI hat.
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

./dot3k_text_run.py

Currently it just prints to the screen, but the commented code will be activated and tested very soon!  (Waiting on my Dothat to arrive).

Example output (shows ipv6 handling, will line wrap IP and netmask if they are longer than 16 chars):
[![solarized dualmode](https://github.com/randomInteger/python_iface_inspector/blob/master/Screen%20Shot%202016-08-28%20at%205.09.54%20PM.png)]
