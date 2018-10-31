from super_bot import SuperBot

class FlyingBot(SuperBot):

  def __init__(self, name, hover=50):
    super().__init__(name)
    self.hover = hover

  def hover(self):
    hover = (int)

  def get_hover_distance(self):
    return self.hover

  def set_hover_distance(self, hover_distance):
    self.hover_distance = hover_distance
