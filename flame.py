#!/usr/bin/env python

import os
import solaredge
import lifxlan
import time

# MAC address of the LIFX light
light_mac_addr = "D0:73:D5:58:AA:DC"

# IP address of the LIFX light
light_ip = "192.168.20.78"

light = lifxlan.TileChain(light_mac_addr, light_ip)
data = light.get_tile_count()
print(f"count: {data}")
data = light.get_canvas_dimensions()
print(f"dims: {data}")
data = light.get_tile_info()
print(f"info: {data}")
#data = light.get_tile_colors(0)
#print(f"tile_colours {data}")
#data = light.get_tilechain_colors()
#print(f"tilechain_colours {data}")


def chaser(bg_colour, colour, i):
  
  matrix = init_matrix(bg_colour)

  matrix[0][i] = (colour, 65535, 65535, 3500)

  try:
    light.set_tilechain_colors(matrix,0,True)
  except:
    print(f"failed")
  finally:
    print(f"finally")


def init_matrix(bg_colour):
  matrix = []
  matrix.append([])

  for i in range(64):
    matrix[0].append((bg_colour, 65535, 65535, 3500))

  return(matrix)

tiles = [
              0,1,
         8, 9, 10,11,12,
         16,17,18,19,20,
         24,25,26,27,28,
         32,33,34,35,36,
         40,41,42,43,44
        ]

for i in tiles:
  chaser(46000, 0, i)
  print(i)
  time.sleep(1)

