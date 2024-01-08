print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

total_occurrence1 = 0
total_occurrence2 = 0

for letter in "true":
    total_occurrence1 += name1.count(letter)
    total_occurrence1 += name2.count(letter)

for letter in "love":
    total_occurrence2 += name1.count(letter)
    total_occurrence2 += name2.count(letter)

score = int(str(total_occurrence1) + str(total_occurrence2))

# Tutorial's solution
# combined_string = name1 + name2
#
# t = combined_string.count("t")
# r = combined_string.count("r")
# u = combined_string.count("u")
# e = combined_string.count("e")
#
# true = t + r + u + e
#
# l = combined_string.count("l")
# o = combined_string.count("o")
# v = combined_string.count("v")
# e = combined_string.count("e")
#
# love = l + o + v + e
#
# score = int(str(true) + str(love))
# Tutorial's solution


if score < 10 or score > 90:
    message = f"Your score is {score}, you go together like coke ane mentos."
elif 40 <= score <= 50:
    message = f"Your score is {score}, you are alright together."
else:
    message = f"Your score is {score}."

print(message)
