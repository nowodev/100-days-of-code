print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Price List
small_pizza, medium_pizza, large_pizza = 15, 20, 25
small_pepperoni, medium_and_large_pepperoni = 2, 3
cheese = 1
bill = 0

# if size == "S":
#     bill += small_pizza
#     if add_pepperoni == "Y":
#         bill += small_pepperoni
#     if extra_cheese == "Y":
#         bill += cheese
#
# elif size == "M":
#     bill += medium_pizza
#     if add_pepperoni == "Y":
#         bill += medium_and_large_pepperoni
#     if extra_cheese == "Y":
#         bill += cheese
#
# elif size == "L":
#     bill += large_pizza
#     if add_pepperoni == "Y":
#         bill += medium_and_large_pepperoni
#     if extra_cheese == "Y":
#         bill += cheese


if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
elif size == "L":
    bill += large_pizza

if add_pepperoni == "Y":
    if size == "S":
        bill += small_pepperoni
    else:
        bill += medium_and_large_pepperoni

if extra_cheese == "Y":
    bill += extra_cheese

print(f"Your final bill is {bill}")
