import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_Squirrel_Data.csv')

grey_squirrels = data[data['Primary Fur Color'] == "Gray"]
cinnamon_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]
black_squirrels = data[data['Primary Fur Color'] == "Black"]

gray_count = grey_squirrels['Primary Fur Color'].count()
cinnamon_count = cinnamon_squirrels['Primary Fur Color'].count()
black_count = black_squirrels['Primary Fur Color'].count()

squirrel_dict = {
    "Fur Color": ['grey', 'cinnamon', 'black'],
    "Count": [gray_count, cinnamon_count, black_count]
}

new_squirrel_data = pandas.DataFrame.from_dict(squirrel_dict)
new_squirrel_data.to_csv('squirrel_count.csv')
