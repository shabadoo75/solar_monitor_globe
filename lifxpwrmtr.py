
from lifxlan import Light

class Lifxpwrmtr(Light):


  def flame_on(self):
    print('flame_on')

  def snap_freeze(self):
    print('snap_freeze')

  def set_heat(self, intensity, magnitude):
    print('set_heat')

  def set_cool(self, intensity, magnitude):
    print('set_cool')
