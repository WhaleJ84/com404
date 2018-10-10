# Ask user for number of robots
print("How many ascii robots should I draw?")
number_robots = int(input())

ROBOT = """ 
#########
#       #
# O   O #
|   V   |
|  ---  |
|_______|
"""
MAX_ROBOTS = 10

# Display robots
if number_robots <= MAX_ROBOTS:
  for count in range(number_robots):
    print(ROBOT)
else:
  for count in range(MAX_ROBOTS):
    print(ROBOT)
