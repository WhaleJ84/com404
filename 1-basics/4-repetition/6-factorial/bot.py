print("Please enter a number:")
number = int(input())

times = 1
sum = 1

for x in range(number): 
  sum = sum * times
  times = times + 1

print("The factorial of your number is:", sum)
