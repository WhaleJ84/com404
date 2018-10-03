# Read current amount from user
print("What is your current amount in savings? (£)")
current_amount = float(input())

# Read interest rate from user
print("What is your interest percentage rate? (%)")
interest_rate = float(input())

# Calculate new amount
interest_amount = (interest_rate / 100) * current_amount
new_amount = current_amount + interest_amount

# Display the result
print("Your savings after one year will be: £" + str(new_amount))
