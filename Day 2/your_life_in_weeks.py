print("Your life in weeks")
age = int(input("How old are you? "))

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# My solution
years_left = 90 - age
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left until 90"
print(message)
