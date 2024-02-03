from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operators:
        print(symbol)
    should_continue = True

    while should_continue:
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operator]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
