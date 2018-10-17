# Created a function to define the parameters of our enigma
def enigma():
  print("Please enter a character to display:")
  character = input()
  print("Please enter total number of characters:")
  char_num = int(input())
  print("Please enter a number:")
  num = int(input())

  counter = 1

  print("Result is:")
  for x in range(0, char_num, 1):
    if counter == num:
      print(character, end="")
      counter = 1
    else:
      print("-", end="")
      counter = counter + 1

enigma()
