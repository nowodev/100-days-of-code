# from turtle import Turtle, Screen
#
# tummy = Turtle()
# tummy.shape("turtle")
# tummy.color("coral")
# tummy.forward(100)
# tummy.left(100)
# tummy.forward(100)
# tummy.left(100)
# tummy.forward(100)
# tummy.left(100)
# tummy.forward(100)
# my_screen = Screen()
#
# print(tummy)
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)

