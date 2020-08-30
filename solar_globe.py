#!/usr/bin/env python

import os
import solaredge
import lifxpwrmtr
from lifxpwrmtr import set_heat

site_id = 1577716
s = solaredge.Solaredge(os.environ['SOLAREDGE_API_KEY'])

data = s.get_current_power_flow(site_id)
pwr_total     = data['siteCurrentPowerFlow']['LOAD']['currentPower']
pwr_from_grid = data['siteCurrentPowerFlow']['GRID']['currentPower']
pwr_from_pv   = data['siteCurrentPowerFlow']['PV']['currentPower']


light = lifxpwrmtr.Light("12:34:56:78:9a:bc", "192.168.1.42")

hue = 0
saturation = 65535
#pwr_total sets brightness
brightness = pwr_total/8 * 65535
kelvin = 0

if pwr_from_grid > 0:
  if pwr_from_grid > 4:
    light.flame_on()
  else:
    light.set_heat(pwr_from_grid, pwr_total)
 # yellow - orange - red - flames!
 # hue 64 -- 0
else:
  if pwr_from_pv > 4:
    light.snap_freeze()
  else:
    light.set_cool(pwr_from_pv, pwr_total)
 # green - cyan - blue - purple/blue
 # hue 128 -- 256

print(f"total power:{pwr_total}")
print(f"power from grid:{pwr_from_grid}")
print(f"power from pv:{pwr_from_pv}")

