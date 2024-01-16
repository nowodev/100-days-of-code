import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

total_names = len(names)
selected_name = random.randint(0, total_names - 1)
payer = names[selected_name]

# payer = random.choice(names) # Easier solution

print(f"{payer} is going to buy the meal today!")


