# Calculate total age
def sum_ages_of_friends(apple_age, rainbow_age, butter_age):
  total_age = (apple_age + rainbow_age + butter_age)
  return(total_age)

# Calculate average age
def calc_avg_age_of_friends(apple_age, rainbow_age, butter_age):
  average_age = (apple_age + rainbow_age + butter_age/ 3)
  return(average_age)

# Run the program
def run():
  print("What is the age of Applejack, Rainbowdash and Buttershine?")
  apple_age = int(input())
  rainbow_age = int(input())
  butter_age = int(input())
  print("Would you like to see the sum or average of the ponies?")
  option = input()
  if option == "sum":
    print(sum_ages_of_friends(apple_age, rainbow_age, butter_age))
  elif option == "average":
    print(calc_avg_age_of_friends(apple_age, rainbow_age, butter_age))
  else:
    print("Error.")

run()
