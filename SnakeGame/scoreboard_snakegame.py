from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_snakegame.txt") as data:
            self.high_score = int(data.read())
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
            with open("data_snakegame.txt", mode="w") as data:
                 data.write(str(self.high_score))
        self.score = 0
        self.score_count()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)
