from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def forward():
    timmy.forward(10)

def backward():
    timmy.backward(10)

def clockwise():
    timmy.right(10)

def counter_clockwise():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.up()
    timmy.home()
    timmy.down()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(clear, "c")








screen.exitonclick()