# Creates a function that asks for an activity
def activity_time():
  print("What activity would you like to do? I have lots of movies and toys to play with.")
  activity = input()
  if activity == "watch movie":
    print("Watching a movie sounds like fun!")
  elif activity == "play":
    print("I have lots of toys to play with!")
  else:
    print("Sorry, I did not catch that.")
  print()

activity_time()
activity_time()
activity_time()
