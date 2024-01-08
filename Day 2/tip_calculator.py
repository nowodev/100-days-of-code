print("Welcome to the tip calculator")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip_amount = bill * tip / 100
total_bill = bill + total_tip_amount
individual_bill = round(total_bill / people, 2)
individual_bill = "{:.2f}".format(individual_bill)

print(f"Each person should pay: {individual_bill}")
