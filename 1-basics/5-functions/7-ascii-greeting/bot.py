# Creates a function to display an ascii box around variables defined in the next function
def display_box(name):
  print("*" * (len(name) + 10))
  print("* Hello", name, "*")
  print("*" * (len(name) + 10))
  
# Creates a function to ask user for their name
def greet_user():
  print("Please enter your name")
  name = str(input())
  display_box(name)
  
greet_user()
