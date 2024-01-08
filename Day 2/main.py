# Data Types
# String
"Hello"[4]
"123"
print("123" + "456")

# Integer
123
456
print(123 + 456)

print(343343434)
print(343_343_434)

# Float
3.14159

# BooleanType Errors
# num_char = len(input("What is your name?\n"))
# print(type(num_char))
#
# # To avoid error, convert variable to string
# # print("Your name has " + num_char + " characters.")
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# Changing data types
a = 123
b = float(a)
c = str(a)

print(type(a))
print(type(b))
print(type(c))

print(70 + float("100.5"))
print(str(70) + str("100"))

# Mathematical operators
# Addition
print(3 + 5)
# Subtraction
print(7 - 4)
# Multiplication
print(3 * 2)
# Division
print(6 / 2)
# Exponential
print(2 ** 3)

# P - PARENTHESIS
# E - EXPONENTIAL
# M - MULTIPLICATION
# D - DIVISION
# A - ADDITION
# S - SUBTRACTION
# L - LEFT TO
# R - RIGHT

print(3 * 3 + 3 / 3 - 3)

# Number Manipulation
# Division always result in a floating point number unless you use the //
print(type(8 // 3))

result = 4 / 2
result /= 2
print(result)

score = 0
score += 5
print("Initial score: " + str(score))
score -= 1
print("Final Score: " + str(score))

# F-String
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height} and your are winning is {isWinning}.")
