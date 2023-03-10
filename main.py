import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

state = turtle.Turtle()
state.hideturtle()
state.penup()
state.speed(0)
state.color("black")

def draw_country(pos, answer):
    state.goto(pos)
    state.write(arg=f"{answer}")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

new_data = pandas.read_csv("50_states.csv")
states_list = new_data.state.to_list()


called_states = []

while len(called_states) < len(states_list):
    answer_state = screen.textinput(title=f"Guess the State {len(called_states)}/{len(states_list)}", prompt="What's another stat's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        called_states.append(answer_state)
        found_state = new_data[new_data.state == answer_state]
        pos = (int(found_state["x"]), int(found_state["y"]))
        print(pos)
        draw_country(pos, answer_state)

# states_to_learn.csv
to_learn = states_list
for state in called_states:
    to_learn.remove(state)
new_data = pandas.DataFrame(to_learn)
new_data.to_csv("states_to_learn.csv")



# turtle.exitonclick()   # it's way to stay open our screen until our code is running
# screen.exitonclick()

