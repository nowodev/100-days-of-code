print("Welcome to the Leap Year Calculator")
year = int(input("Which year do you want to check? "))

# A leap year is one that's:
# Evenly divisible by 4
# Not evenly divisible by 100
# Evenly divisible by 400

# It's a leap year if it's divisible by 4 without remainder,
# For centennial years, i.e. every 100 years (1700, 1800, 1900, 2000)
# If it's divisible by 400 without remainder
# For other years, if it's also divisible by 100 & 400
# and the remainder is an even number, then it's a leap year

# My solution
# if year % 4 == 0:
#     # For centennial years
#     if year % 100 == 0:
#         print("It's a centennial year")
#         if year % 400 == 0:
#             print(f"The year {year} is a leap year")
#         else:
#             print(f"The year {year} is not a leap year")
#     else:
#         print(f"The year {year} is a leap year")
# else:
#     print(f"The year {year} is not a leap year")

# Allianora's solution
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
