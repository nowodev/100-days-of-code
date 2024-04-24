with open("./Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
    for name in names:
        new_letter = letter.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as mail:
            mail.write(new_letter)
