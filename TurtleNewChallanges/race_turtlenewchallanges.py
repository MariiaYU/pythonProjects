from turtle import Turtle, Screen
import random


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a rainbow color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


if user_bet:
    race_on = True

turtle_list = []
y = -125
for x in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y += 50
    turtle_list.append(new_turtle)

def win_turtle():
    while race_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                return turtle.pencolor()
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


write_turtle = Turtle()
write_turtle.hideturtle()

if win_turtle()==user_bet:
    screen.clear()
    write_turtle.write("You win!", align="center", font=('Arial', 20, 'normal'))
else:
    screen.clear()
    write_turtle.write(f"Turtle with {win_turtle()} color win. You lose!", align="center", font=('Arial', 20, 'normal'))



















screen.exitonclick()