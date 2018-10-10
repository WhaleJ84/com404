print("Please enter a word")
userWord = str(input())

for position in reversed(range(0, len(userWord), 1)):
	print(userWord[position])
