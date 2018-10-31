from bot import Bot
from flying_bot import FlyingBot
from super_bot import SuperBot

walle = Bot("WallE")

walle.display_name()
walle.display_age()
walle.display_energy()
walle.display_shield()
print()

rob = SuperBot("ROB")

print("The {}'s power level is: {}".format(rob.get_name(), rob.get_super_power_level()))
print()

alex = FlyingBot("Alex Murphy")

print("{}'s hover distance is: {}".format(alex.get_name(), alex.get_hover_distance()))
print()
