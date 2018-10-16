NUM = 7
INPUT = NUM     #Stays the same
counter = NUM   #Should be 0
row = 0       #Should be same as input
rowColumn = 0 #Should be same as input

while row != INPUT:
    if row == 0: #completes first row
        print(counter)
        counter = counter - 1
        row = row + 1
    elif row >= 1: #completes other rows
        if row != counter:
            rowColumn = 0
            print(counter, "", end='')
            rowColumn = rowColumn +1
            print((counter + INPUT) * rowColumn)
            rowColumn = rowColumn + 1 #If rowColumn == row = ((counter + INPUT) * row)
            #print((counter + INPUT) ** rowColumn)
            counter = counter - 1
            row = row + 1
        #elif: # If rowColumn != row = new line.
    else:
        break

print()
print(INPUT, counter, row, rowColumn)
