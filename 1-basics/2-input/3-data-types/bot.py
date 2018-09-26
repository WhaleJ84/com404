# Ask user for data
print("What is your name?")
name = input()

print("How old are you (years)?")
age = int(input())

print("How much do you weigh (kg)?")
weight = float(input())

print("How tall are you (m)?")
height = float(input())

print("Calculating bmi...")
bmi = weight / (height * height)
print("Your bmi is", bmi)
