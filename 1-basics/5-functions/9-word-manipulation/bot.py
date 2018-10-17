def display_box(word):
  print("*" * (len(word) + 10))
  print("*", word, "*")
  print("*" * (len(word) + 10)) 

def display_lower(word):
  lower_text = (word.lower())
  return(lower_text)

def display_upper(word):
  upper_text = (word.upper())
  return(upper_text)

def display_mirror(word):
  reverseWord = str()
  for position in range(len(word) -1, -1, -1):
    print(word[position], end="")

#def display_repeat(word):

#print("Please enter a word:")
#word = input()
#print(
#  """Please choose one of the following options:
#  Display in a box
#  Display lower-case
#  Display upper-case
#  Display mirrored
#  Repeat
#  """)
#option = input()

word = "TeStWoRd"
option = "Display in a box"

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
