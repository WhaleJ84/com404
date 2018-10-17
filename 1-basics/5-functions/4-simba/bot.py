# Creates a function to determine Simba's roar output
def roar(num_roars):
  print("Simba says:")
  for tries in range(num_roars, 0, -1):
    print("roar!")
  if num_roars < 3:
    print("cough! cough!")
  else:
    print("ROAR!!!")
  print()
  
# The following are calls to the function for testing purposes
roar(1)
roar(3)
