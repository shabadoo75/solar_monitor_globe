import random
from lifxlan import Light, BLUE, RED

kelvin = 4500
transition_time = 3000

class Light(Light):

  ##
  # flame effect when drawing above max power from the grid
  def flame_on(self):
    print('flame_on')
    self.set_color(RED, transition_time)

  ##
  # blizzard effect when feeding in above max power to the grid
  def blizzard(self):
    print('snap_freeze')
    self.set_color(BLUE, transition_time)

  ##
  # hot colours, for when you're drawing power from the grid
  # intensity - number between 0 - 100 indicating how much power
  #             the house is drawing from the grid
  # magnitude - number beween 0 - 100 indicating the total amount
  #             of power the house is using, grid + solar
  def set_heat(self, intensity, magnitude):
    print(f"set_heat {intensity} : {magnitude}")
    start_hue = 64 # yellow
    end_hue = 0 # red

    hue = ((start_hue - (intensity * (start_hue/100)))/360) * 65535
    saturation = 65535
    brightness = 65535 * (magnitude/100)
    colour = [hue, saturation, brightness, kelvin]
    print(colour)
    self.set_color(colour, transition_time)
    # yellow - orange - red - flames!
    # hue 64 -- 0

  def set_cool(self, intensity, magnitude):
    print(f"set_cool {intensity} : {magnitude}")
    start_hue = 128 # green
    end_hue = 256 # blue

    hue = ((start_hue + (intensity * (end_hue - start_hue)/100))/360) * 65535
    saturation = 65535
    brightness = 65535 * (magnitude/100)
    colour = [hue, saturation, brightness, kelvin]
    print(colour)
    self.set_color(colour, transition_time)
    # green - cyan - blue - purple/blue
    # hue 128 -- 256

  def set_white(self, magnitude):
    print(f"set white {magnitude}")

    brightness = 65535 * (magnitude/100)
    colour = [58275, 0, brightness, kelvin]
    self.set_color(colour, transition_time)
