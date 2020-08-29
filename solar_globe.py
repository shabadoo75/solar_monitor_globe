#!/usr/bin/env python

import os
import solaredge
import lifxlan


s = solaredge.Solaredge(os.environ['SOLAREDGE_API_KEY'])

data = s.get_current_power_flow(1577716)
pwr_total     = data['siteCurrentPowerFlow']['LOAD']['currentPower']}
pwr_from_grid = data['siteCurrentPowerFlow']['GRID']['currentPower']}
pwr_from_pv   = data['siteCurrentPowerFlow']['PV']['currentPower']}


lan = lifxlan.LifxLAN()
light = lifxlan.Light("12:34:56:78:9a:bc", "192.168.1.42")
light.set_power(power, [duration], [rapid])
light.set_color(color, [duration], [rapid])

hue = 0
saturation = 65535
#pwr_total sets brightness
brightness = pwr_total/8 * 65535
kelvin = 0

if pwr_from_grid > 0:
 # yellow - orange - red - flames!
else:
 # green - cyan - blue - purple/blue

print(f"total power:{pwr_total}")
print(f"power from grid:{pwr_from_grid}")
print(f"power from pv:{pwr_from_pv}")

