print("How many ascii robots should I draw?")
number_robots = int(input())

robot = """ 
#########
#       #
# O   O #
|   V   |
|  ---  |
|_______|
"""

if number_robots <= 10:
  for count in range(number_robots):
    print(robot)
else:
  for count in range(10):
    print(robot)
