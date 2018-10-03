# 
print("Where should I look?")
print("Your options are:")
print("In the bedroom")
print("In the bathroom")
print("In the lab")

look = input()

if (look == "In the bedroom"):
  print("In the bedroom you see something under the bed.")
  print("Where should I look?")
  bedroom_look = input()
  if (bedroom_look == "Under the bed"):
    print("Found some socks but no battery.")
  else:
    print("Found some mess but no battery.")
elif (look == "In the bathroom"):
  print("In the bathroom you see something under the bathtub.")
  print("Where should I look?")
  bathroom_look = input()
  if (bathroom_look == "Under the bathtub"):
    print("Found a rubber duck but no battery.")
  else:
    print("It's wet and there is no battery.")
elif (look == "In the lab"):
  print("In the lab you see something on the table.")
  print("Where should I look?")
  lab_look = input()
  if (lab_look == "On the table"):
    print("Found the battery!")
  else:
    print("Found some tools but no battery.")
else:
  print("I don't know where that is but I will keep looking.")
