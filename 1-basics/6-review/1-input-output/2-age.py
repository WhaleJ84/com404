DAYS_IN_YEAR =  365.25

# Determine someones age in days
print("Please enter your age (years)")
age_in_years = float(input())

age_in_days = age_in_years * DAYS_IN_YEAR

#age_in_days = age_in_years * 365.25
# YEAR = 365
#age_in_days = age_in_years * year

print("You are", round(age_in_days), "days old.")
