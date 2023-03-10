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

def draw_country(pos, state):
    state.goto(pos)
    state.write(arg=f"{state}")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)


answer_state = screen.textinput(title="Guess the State", prompt="What's another stat's name?").capitalize()
print(answer_state)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()




print(states_list)
if answer_state in states_list:
    found_state = data[data.state == answer_state]
    pos = (found_state[x], found_state[y])
    print(pos)
    # draw_country(pos, answer_state)



turtle.mainloop()   # it's way to stay open our screen until our code is running



# screen.exitonclick()

