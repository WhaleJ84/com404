def display_box(word):
  print("*" * (len(word) + 4))
  print("*", word, "*")
  print("*" * (len(word) + 4), end="") 
  return("")

def display_lower(word):
  lower_text = (word.lower())
  return(lower_text)

def display_upper(word):
  upper_text = (word.upper())
  return(upper_text)

def display_mirror(word):
  print(word, "| ", end="")
  for position in range(len(word) -1, -1, -1):
    print(word[position], end="")
  return("")

def display_repeat(word):
  print("How many times would you like to display the word?")
  LOOP = int(input())
  for count in range(LOOP):
    if count % 2 == 0:
      print(word.lower(), end="")
    else:
      print(word.upper(), end="")
  return("")

def run():
  print("Please enter a word:")
  word = input()
  print(
  """Please choose one of the following options:
  Display in a box
  Display lower-case
  Display upper-case
  Display mirrored
  Repeat
  """)
  option = input()

  if option == "Display in a box":
    print(display_box(word))
  elif option == "Display lower-case":
    print(display_lower(word))
  elif option == "Display upper-case":
    print(display_upper(word))
  elif option == "Display mirrored":
    print(display_mirror(word))
  elif option == "Repeat":
    print(display_repeat(word))
  else:
    print("Error.")

run()
