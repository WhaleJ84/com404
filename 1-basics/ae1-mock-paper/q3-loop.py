# Q3) Loop

print("Please enter a whole number:")
num = int(input())
print("Counting down...")

# takes input number and prints a countdown from that.
for x in (range(num, -1, -1)):
  print(x)
