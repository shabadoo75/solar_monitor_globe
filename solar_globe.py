#!/usr/bin/env python

import os
import solaredge
import lifxpwrmtr

# solaredge site ID
site_id = 1577716

# max power difference
# value in kW that is considered max in terms of the colour scales
# i.e if it's set to 4 then drawing 4kW from the grid is the top
# of the scale, anything above that makes the light flame.
# Likewise if we're putting 4kW from PV back into the grid then
# that is considered max, anything above that is blizzard! 
max_pwr_diff = 4

# Value in kW that is considered the maximum power we draw in total
# This value is used to set the brightness. e.g. if this is set to
# 8 then when we're drawing 8kW or above the glove is at max brightness
max_pwr_total = 8

s = solaredge.Solaredge(os.environ['SOLAREDGE_API_KEY'])

data = s.get_current_power_flow(site_id)
pwr_total     = data['siteCurrentPowerFlow']['LOAD']['currentPower']
pwr_from_grid = data['siteCurrentPowerFlow']['GRID']['currentPower']
pwr_from_pv   = data['siteCurrentPowerFlow']['PV']['currentPower']
pwr_to_grid   = max(0, pwr_from_pv - pwr_total)


light = lifxpwrmtr.Light("12:34:56:78:9a:bc", "192.168.1.42")

#pwr_total sets brightness
brightness = pwr_total/max_pwr_total * 100

if pwr_from_grid > 0:
  intensity = min(100, pwr_from_grid / max_pwr_diff * 100)

  if pwr_from_grid > max_pwr_diff:
    light.flame_on()
  else:
    light.set_heat(intensity, brightness)
else:
  intensity = min(100, pwr_to_grid / max_pwr_diff * 100)

  if pwr_to_grid > max_pwr_diff:
    light.blizzard()
  else:
    light.set_cool(intensity, brightness)

print(f"total power:{pwr_total}")
print(f"power from grid:{pwr_from_grid}")
print(f"power from pv:{pwr_from_pv}")
print(f"power to grid:{pwr_to_grid}")

