import random
from art import logo

print(logo)


def set_difficulty(level):
    """Return available attempts for the difficulty level."""
    if level == "easy":
        return difficulty["easy"]
    else:
        return difficulty["hard"]


def check_answer(guess, number, attempts):
    """Checks answer against guess. Returns the number of attempts remaining"""
    if guess > number:
        print("Too high.\nGuess again.")
        return attempts - 1
    elif guess < number:
        print("Too low.\nGuess again.")
        return attempts - 1
    else:
        print(f"You got it! The number was {number}")
        return attempts - attempts


print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

difficulty = {"easy": 10, "hard": 5}
generated_number = random.randint(1, 100)

attempts = set_difficulty(difficulty_level)

while attempts != 0:
    print(f"You have {attempts} attempts to guess the number")
    guessed_number = int(input("Make a guess: "))
    attempts = check_answer(guessed_number, generated_number, attempts)
