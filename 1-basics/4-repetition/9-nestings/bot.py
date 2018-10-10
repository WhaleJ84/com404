print("Please enter a sequence:")
sequence = input()
print("Please enter the marker:")
marker = input()

start_marker = -1
end_marker = -1

for position in range(0, len(sequence), 1):
  letter = sequence[position]

  if (letter == marker):
    if (start_marker == -1):
      start_marker = position
    else:
      stop_marker = position

print(("The difference is:", stop_marker - start_marker -1))
