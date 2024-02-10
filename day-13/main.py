############DEBUGGING#####################

# # Describe Problem
# def my_function():
#     """The problem is the range function doesn't read the last argument hence
#     the for loop stops at 19"""
#     # for i in range(1, 20):
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 6)
# dice_num = randint(0, 5)
# """The dice_imgs has 6 items but it's from 0 - 5. Hence if dice_num is returned
# as 6, then it will be out of index as there are only 6 items not 7."""
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# """There is a bug when you enter 1994, because the current checks for dates between 1980 and 1994,
# that is from 1981 to 1993"""
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# # elif year > 1994:
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# # age = input("How old are you?")
# age = int(input("How old are you? "))
# if age > 18:
#     # print("You can drive at age {age}.")
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))
# print(pages)
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
# # b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
