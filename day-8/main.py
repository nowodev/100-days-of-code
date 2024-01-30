# Simple function
def greet():
    print("Hello Tolu")
    print("How do you do Jack Bauer")
    print("Isn't the weather nice today?")


greet()


# Functions that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Tolu")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}, what is it like in {location}")


# Function with positional argument
greet_with("Jack Bauer", "Nowhere")

# Function with keyword argument
greet_with(location="Nowhere", name="Jack Bauer")
