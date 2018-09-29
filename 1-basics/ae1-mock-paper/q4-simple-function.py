# Q4) Simple function

print("Please enter your first number:")
num1 = int(input())

print("Please enter your second number:")
num2 = int(input())

#works out the difference between both numbers
def displaySmallest(num1, num2):
  if (num1 < num2):
    print("The first number is smaller")
  elif (num1 > num2):
    print("The second number is smaller")
  else:
    print("Both numbers are equal")

displaySmallest(num1,num2)
