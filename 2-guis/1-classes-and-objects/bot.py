class Bot:

  def __init__(self, name, age=0, energy=100,shield=100):
    self.name = name
    self.age = age
    self.energy = energy
    self.shield = shield

  def get_age(self):
    return self.age

  def get_energy(self):
    return self.energy

  def get_name(self):
    return self.name 

  def get_shield(self):
    return self.shield

  def decrement_energy(energy_decrease):
    energy = (self.energy - energy_decrease)

  def decrement_shield(shield_decrease):
    shield = (self.shield - shield_decrease)

  def display_name(self):
    print("The robot's name is: {}".format(self.name))

  def display_age(self):
    print("The robot's age is: {}".format(self.age))

  def display_energy(self):
    print("The robot's energy is: {}".format(self.energy))

  def display_shield(self):
    print("The robot's shield is: {}".format(self.shield))

  def increment_age(self, age_increase):
    age = (self.age + age_increase)

  def increment_energy(self, energy_increase):
    energy = (self.energy + energy_increase)

  def incrememnt_shield(self, shield_increase):
    shield = (self.shield + shield_increase)

  def set_name(self, name):
    self.name = (name)
