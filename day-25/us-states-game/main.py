import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
states_count = len(data)
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's the state name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()

# screen.exitonclick()
