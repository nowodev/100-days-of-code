# Scope
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function {enemies}")


increase_enemies()
print(f"enemies outside function {enemies}")

# Local Scope
print("Local Scope")


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength)


# Global Scope
print("Global Scope")
player_health = 10  # Global variable


def drink_potion():
    potion_strength = 2  # Local variable
    print(player_health)


drink_potion()

# There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

"""
If you create a variable within a function, then 
it's only available within that function.
"""


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)


create_enemy()

# Modifying Global Scope
print("Modifying Global Scope")

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function {enemies}")


increase_enemies()
print(f"enemies outside function {enemies}")

"""
It's advisable not to modify global variable
"""


def increase_enemies():
    print(f"enemies inside function {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"New enemies {enemies}")

# Global Constants
PI = 3.141592653589793
URL = "https://adventofcode.com"
TWITTER_HANDLE = "@farvyy"
