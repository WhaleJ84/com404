# Ask the user for two numbers 
print("Please enter the first number:")
first_number = float(input())

print("Please enter the second number:")
second_number = float(input())

# Compares the two numbers
if (first_number > second_number):
  print("The first number is bigger.")
elif (first_number < second_number):
  print("The second number is bigger.")
else:
  print("Both numbers are equal.") 
