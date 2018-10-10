print("Please enter a word")
userWord = str(input())

reverseWord = str()
for position in range(len(userWord) -1, -1, -1):
  print(userWord[position], end="")
