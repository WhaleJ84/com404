from bot import Bot

class SuperBot(Bot):

  def __init__(self, name, super_power_level=10):
    super().__init__(name)
    self.super_power_level = super_power_level

  def super_power_level(self):
    super_power_level = (int)

  def get_super_power_level(self):
    return self.super_power_level

  def set_super_power_level(self, power_level):
    self.super_power_level = power_level
