# with open('./weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#
# print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(f"Average temperature: {average_temp}")
# print(f"Average temperature: {data['temp'].mean()}")
#
# print(f"Max temperature: {data['temp'].max()}")
#
# # Get data in Columns
# print(data['condition'])
# print(data.condition)

# Get data in Rows
print(data[data.day == 'Monday'])

# Get row with the highest temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)
print(f"In Fahrenheit: {(monday.temp * 9 / 5) + 32}")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Bob", "Charlie"],
    "grades": [90, 80, 70]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")
