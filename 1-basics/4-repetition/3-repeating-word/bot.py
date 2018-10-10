# Ask user to input a word
print("Please enter a word for me to learn:")
word = input()

# Use the len function to work out number of letters
letter_count = len(word)

# Print the word as many times are there are letters in the word
for count in range(letter_count):
  print(word)
