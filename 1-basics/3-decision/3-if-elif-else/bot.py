#  Read direction from user
print("Please enter one of the following directions: (w,a,s or d)")

direction = input()

# Work out which direction to move
if (direction == "w"):
  print("I am moving up.")
elif (direction == "a"):
  print("I am moving left.")
elif (direction == "s"):
  print("I am moving down.")
elif (direction == "d"):
  print("I am moving right.")
else:
  print("I am not sure which direction to move in.")
