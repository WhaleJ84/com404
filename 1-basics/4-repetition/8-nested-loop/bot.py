# Ask the user how many rows and columns they want
print("How many rows should I have?")
rows = int(input())
print("How many columns should I have?")
columns = int(input())

asciiFace = ":-) "

# Print an ascii face in the rows and columns defined above
print("Here I go:")
for count in range(rows):
  for number in range(columns):
    print(asciiFace, end="")
  print()

print("Done!")
