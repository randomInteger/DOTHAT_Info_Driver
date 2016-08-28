# python_iface_inspector
Simple example python code to inspect interfaces (as well as some other bonus data) and format the output. Intended as a template for data shown on a 16x3 Raspberry PI display such as the Pimoroni Display-o-Tron Hat.

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

Example output:
[![solarized dualmode](https://github.com/randomInteger/python_iface_inspector/blob/master/Screen%20Shot%202016-08-27%20at%205.13.02%20PM.png)]
