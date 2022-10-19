from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.hideturtle()
        self.goto(y=270, x=0)
        self.color("white")
        self.write(f"Score is: {self.number}", align=ALIGN, font=FONT)

    def score_count(self):
        self.number += 1
        self.clear()
        self.write(f"Score is: {self.number}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
