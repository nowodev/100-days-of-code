MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

change = 0
money = 0


def show_ingredients(ingredients):
    """Returns the ingredients on separate lines"""
    return (
        f"Water: {ingredients['water']}ml\n"
        f"Milk: {ingredients['milk']}ml\n"
        f"Coffee: {ingredients['coffee']}g\n"
        f"Money: ${money}"
    )


def is_resource_sufficient(ingredients):
    """Checks if the ingredients are sufficient"""
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False

    return True


def process_coins():
    """Converts all inserted coins to the nearest dollar"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies


def is_transaction_successful(drink_cost, payment):
    """Checks if the transaction is successful"""
    if payment >= drink_cost:
        change = inserted_coins - drink_cost
        print(f"Here is ${change:.2f} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_type):
    """Make the coffee and reduce the available resources"""
    for ingredient in MENU[coffee_type]['ingredients']:
        resources[ingredient] -= MENU[coffee_type]['ingredients'][ingredient]
    print(f"Here's your {choice} ☕️ Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(show_ingredients(resources))
    elif choice == "off":
        is_on = False
    else:
        coffee = MENU[choice]
        if is_resource_sufficient(coffee['ingredients']):
            inserted_coins = process_coins()
            if is_transaction_successful(coffee['cost'], inserted_coins):
                make_coffee(choice)
