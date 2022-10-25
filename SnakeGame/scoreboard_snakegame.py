from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.goto(y=270, x=0)
        self.color("white")
        self.score_count()

    def score_count(self):
        self.clear()
        self.write(f"Score is: {self.score} | High score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_count()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)
