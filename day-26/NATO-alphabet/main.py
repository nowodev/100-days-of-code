import pandas

student_dict = {
    "student": ["Angela", "Bob", "Charlie"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key, value)


# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# # Loop through a data frame
# for key, value in student_data_frame.items():
#     print(key)
#     print(value)

# for (index, row) in student_data_frame.iterrows():
#     print(row)
#     print(row.student)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a name: ").upper()

output = [nato_dict[letter] for letter in word]
print(output)
