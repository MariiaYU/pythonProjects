from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def update_score_board(self):
        self.clear()
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_level(self):
        self.level += 1


