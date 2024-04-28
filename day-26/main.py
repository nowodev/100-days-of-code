numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [n + 1 for n in numbers]

name = "Toluwani"
new_name_list = [letter for letter in name]

new_range_list = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names_in_caps = [name.upper() for name in names if len(name) > 5]

# Exercise 1
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in nums]

# Exercise 2
result = [num for num in nums if num % 2 == 0]

# Exercise 3
with open("file1.txt") as file1, open("file2.txt") as file2:
    file1 = file1.readlines()
    file2 = file2.readlines()

file_result = [int(num) for num in file1 if num in file2]
print(file_result)

# result = [num for num in nums if num % 2 == 0]

# print("New list: ", new_list)
# print("New names: ", new_name_list)
# print("New range: ", new_range_list)
# print("Short names: ", short_names)
# print("Long names in caps: ", long_names_in_caps)
# print("Square numbers: ", squared_numbers)
# print("Result: ", result)
