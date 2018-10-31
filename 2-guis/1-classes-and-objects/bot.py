class Bot:

  def __init__(self, name):
    self.name = name
    self.age = 0
    self.energy = 100
    self. shield = 100

  def display_name(self):
    print(self.name)

  def display_age(self):
    print(self.age)

  def display_energy(self):
    print(self.energy)

  def display_shield(self):
    print(self.shield)

  def display_summary(self):
    print("{} is {} years old and has {} energy and {} shield remaining.".format(self.name,self.age,self.energy,self.shield))

  def __str__(self):
    return("{} is {} years old and has {} energy and {} shield remaining.".format(self.name,self.age,self.energy,self.shield))
  
  
  
from bot import Bot

walle = Bot("WallE")

walle.display_name()
walle.display_age()
walle.display_energy()
walle.display_shield()
walle.display_summary()
