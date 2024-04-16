# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

"""
If you forget to close the files, you can use this alternative method of opening files.
"""

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("my_file.txt", mode="a") as write_file:
#     write_file.write("\nI love Python.")