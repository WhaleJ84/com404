# Read user numbers
print("Please enter first number:")
first_number = int(input())

print("Please enter second number:")
second_number = int(input())

print("Please enter third number:")
third_number = int(input())

total_odd = 0
total_even = 0

# Compares numbers to check if they are even or odd
if (first_number % 2 == 0):
  total_even = (total_even + 1)
else:
  total_odd = (total_odd + 1)

if (second_number % 2 == 0):
  total_even = (total_even + 1)
else:
  total_odd = (total_odd + 1)

if (third_number % 2 == 0):
  total_even = (total_even + 1)
else:
  total_odd = (total_odd + 1)

print("You have entered", total_odd, "odd and", total_even, "even numbers.")
