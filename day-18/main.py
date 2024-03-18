from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
tim.shape("turtle")
tim.color("red")

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


"""Challenge 1"""
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
#
#
"""Challenge 2"""
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


"""Challenge 3"""
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

"""Challenge 4"""
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     # tim.color(random.choice(colors))
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


"""
Challenge 5
Draw a circle / make a spirograph
"""
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
