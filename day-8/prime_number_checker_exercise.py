# Write your code below this line 👇

print("Welcome to The Prime Number Checker")


# My Solution
# def prime_checker(number):
#     if number in [2, 3, 5]:
#         print("It's a prime number.")
#     elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")


# Angela's Solution
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
