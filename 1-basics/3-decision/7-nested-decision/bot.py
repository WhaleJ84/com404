# Ask the user where to look
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
