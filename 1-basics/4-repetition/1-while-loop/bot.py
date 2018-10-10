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

robots_displayed = 0
MAX_ROBOTS = 10

# Display robots
if number_robots <= MAX_ROBOTS:
  while robots_displayed < (number_robots):
    print(ROBOT)
    robots_displayed = robots_displayed + 1
else:
  while robots_displayed < MAX_ROBOTS:
    print(ROBOT)
    robots_displayed = robots_displayed + 1
