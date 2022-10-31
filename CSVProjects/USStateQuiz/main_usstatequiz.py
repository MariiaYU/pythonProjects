import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_of_all_states = data["state"].to_list()


def user_state(state):
    state_data = data[data.state == f"{state}"]
    y_cor = int(state_data.y)
    x_cor = int(state_data.x)
    return x_cor, y_cor


def write_state_name(coordinate, user_answer):
    user_state = turtle.Turtle()
    user_state.penup()
    user_state.hideturtle()
    user_state.goto(coordinate)
    user_state.write(user_answer, font=('Arial', 8, 'normal'))


how_many_states = data.state.count()
how_many_user_guessed = 0
all_user_states = []
game_is_on = True
while game_is_on:
    answer_state = (screen.textinput(title=f"Guess the State: {how_many_user_guessed}/{how_many_states}",
                                     prompt="What is another state name?")).title()
    if answer_state in list_of_all_states:
        if answer_state not in all_user_states:
            all_user_states.append(answer_state)
            state_coordinate = user_state(answer_state)
            write_state_name(state_coordinate, answer_state)
            how_many_user_guessed += 1

    if how_many_user_guessed == how_many_states:
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(0, 260)
        text.write("You have guessed all US States!", align="center", font=('Arial', 30, 'normal'))
        game_is_on = False

turtle.mainloop()
