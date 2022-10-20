from turtle import Screen
from elements_pingpong import Paddle, Ball, SeparateLine
from scoreboard_pingpong import ScoreBoard
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

sep_line = SeparateLine()


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

score_board = ScoreBoard()

ball_speed = 0.09


game_is_on = True
while game_is_on:
    score_board.update_score_board()
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        ball_speed *= 0.9
    elif ball.xcor() > 450:
        score_board.l_score += 1
        ball.ball_to_another_player()
    elif ball.xcor() < -450:
        score_board.r_score += 1
        ball.ball_to_another_player()





















screen.exitonclick()