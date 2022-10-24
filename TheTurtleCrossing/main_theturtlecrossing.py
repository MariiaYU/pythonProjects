import time
from turtle import Screen
from player_theturtlecrossing import Player, Turtle
from carmanager_theturtlecrossing import CarManager
from scoreboard_theturtlecrossing import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "space")

car = CarManager()

board = Scoreboard()

num = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    board.update_score_board()
    screen.update()
    if num % 6 == 0:
        car.create()
    car.move()
    num += 1

    for thing in car.all_cars:
        if thing.distance(player) < 20:
            game_over = Turtle()
            game_over.hideturtle()
            game_over.write("GAME OVER", align="center", font=("Courier", 20, "normal"))
            game_is_on = False

    if player.ycor() >= 280:
        car.add_speed()
        board.add_level()

screen.exitonclick()







