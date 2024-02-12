from art import logo, vs
from game_data import data
import random


def get_random_data():
    selected_data = random.choice(data)
    data.remove(selected_data)
    return selected_data


def calculate_score(selected_choice, alternative_choice):
    if selected_choice > alternative_choice:
        return True
    else:
        return False


print(logo)
a = get_random_data()
score = 0
is_correct = True

while is_correct:
    b = get_random_data()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    selected_value = a if choice == "a" else b
    second_value = b if choice == "a" else a
    is_correct = calculate_score(selected_value['follower_count'], second_value['follower_count'])

    if is_correct:
        score += 1
        a = selected_value
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
