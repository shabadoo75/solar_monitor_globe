import random
from lifxlan import Light, BLUE, RED

kelvin = 4500

class Light(Light):

  #def __init__(self, mac_addr, ip_addr, service=1, port=56700, source_id=random.randrange(2, 1 << 32), verbose=False):
  #  super().__init__(mac_addr, ip_addr, service, port, source_id, verbose)

  def flame_on(self):
    print('flame_on')
    self.set_color(RED, 3000)

  def blizzard(self):
    print('snap_freeze')
    self.set_color(BLUE, 3000)

  def set_heat(self, intensity, magnitude):
    print(f"set_heat {intensity} : {magnitude}")

    hue = ((64 - (intensity * (64/100)))/360) * 65535
    saturation = 65535
    brightness = 65535 * (magnitude/100)
    colour = [hue, saturation, brightness, kelvin]
    print(colour)
    self.set_color(colour, 3000)
    # yellow - orange - red - flames!
    # hue 64 -- 0

  def set_cool(self, intensity, magnitude):
    print(f"set_cool {intensity} : {magnitude}")

    hue = ((128 + (intensity * 128/100))/360) * 65535
    saturation = 65535
    brightness = 65535 * (magnitude/100)
    colour = [hue, saturation, brightness, kelvin]
    print(colour)
    self.set_color(colour, 3000)
    # green - cyan - blue - purple/blue
    # hue 128 -- 256

  def set_white(self, magnitude):
    print(f"set white {magnitude}")

    brightness = 65535 * (magnitude/100)
    colour = [58275, 0, brightness, kelvin]
    self.set_color(colour, 3000)
