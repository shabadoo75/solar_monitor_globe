# Solar monitoring globe

Turn your LIFX smart globe into a solar power and grid consumption indicator!

The globe will change colour smoothly from yellow through orange to red as you draw more power from the grid, and from green through cyan to blue the more power your solar system puts back in. The amount of power that your house is using determines the brightness.

Currently only works with SolarEdge inverters

## setup

The monitor requires python3 and a few libraries to run, the easiest way to get up and running is though a python virtual environment:

    python3 -m venv ~/venv/solar
    pip install solaredge
    pip install wheel
    pip install lifxlan

edit solar_globe.py to add your Solaredge siteid, LIFX MAC address and IP

create an environment variable SOLAREDGE_API_KEY with the value of yor API key

then run solar_globe.py in a loop. e.g.

    while true; do ./solar_globe.py; sleep 10; done
