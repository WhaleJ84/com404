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

count = 0

if number_robots <= 10:
  while count < (number_robots):
    print(robot)
    count = count + 1
else:
  while count < (10):
    print(robot)
    count = count + 1
