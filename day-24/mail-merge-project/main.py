with open("Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()

    with open("Input/Names/invited_names.txt") as names:
        names = names.readlines()

        for name in names:
            new_letter = letter.replace("[name]", name.strip())
            print(new_letter)

            mail = open(f"Output/ReadyToSend/letter_for_{name}.txt", "w")
            mail.write(new_letter)
            mail.close()
