from turtle import Screen
from elements_pingpong import Paddle, Ball
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

paddle_right = Paddle()
paddle_left = Paddle()
paddle_right.paddle_creation(x=350, y=0)
paddle_left.paddle_creation(x=-350, y=0)

ball = Ball()


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()







screen.exitonclick()