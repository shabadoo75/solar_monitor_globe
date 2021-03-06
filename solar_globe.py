#!/usr/bin/env python

import os
import solaredge
import lifxpwrmtr

# solaredge site ID
site_id = 1577716

# MAC address of the LIFX light
light_mac_addr = "D0:73:D5:58:AA:DC"

# IP address of the LIFX light
light_ip = "192.168.20.78"

# max power difference
# value in kW that is considered max in terms of the colour scales
# i.e if it's set to 4 then drawing 4kW from the grid is the top
# of the scale, anything above that makes the light flame.
# Likewise if we're putting 4kW from PV back into the grid then
# that is considered max, anything above that is blizzard! 
max_pwr_diff = 4

# Value in kW that is considered the maximum power we draw in total
# This value is used to set the brightness. e.g. if this is set to
# 8 then when we're drawing 8kW or above the globe is at max brightness
max_pwr_used = 8

s = solaredge.Solaredge(os.environ['SOLAREDGE_API_KEY'])

data = s.get_current_power_flow(site_id)
#print(data)

# When there's no flow to or from the grid nothing comes
# back in the 'connections' array so initialize here
pwr_from_grid = 0
pwr_to_grid   = 0

for c in data['siteCurrentPowerFlow']['connections']:

  # flow is from house --> grid
  if c['from'].lower() == 'load' and c['to'].lower() == 'grid':
    pwr_from_grid = 0 
    pwr_to_grid = data['siteCurrentPowerFlow']['GRID']['currentPower']

  # flow is from grid --> house
  if c['from'].lower() == 'grid' and c['to'].lower() == 'load':
    pwr_from_grid = data['siteCurrentPowerFlow']['GRID']['currentPower']
    pwr_to_grid = 0

pwr_used     = data['siteCurrentPowerFlow']['LOAD']['currentPower']
pwr_from_pv   = data['siteCurrentPowerFlow']['PV']['currentPower']

print(f"power used:{pwr_used}")
print(f"power from grid:{pwr_from_grid}")
print(f"power from pv:{pwr_from_pv}")
print(f"power to grid:{pwr_to_grid}")

light = lifxpwrmtr.Light(light_mac_addr, light_ip)

#pwr_used sets brightness
brightness = pwr_used/max_pwr_used * 100

if pwr_from_grid > 0:
  intensity = min(100, pwr_from_grid / max_pwr_diff * 100)

  if pwr_from_grid > max_pwr_diff:
    light.flame_on()
  else:
    light.set_heat(intensity, brightness)

elif pwr_to_grid > 0:
  intensity = min(100, pwr_to_grid / max_pwr_diff * 100)

  if pwr_to_grid > max_pwr_diff:
    light.blizzard()
  else:
    light.set_cool(intensity, brightness)

# power generation exactly balances load
else:
  light.set_white(brightness)

