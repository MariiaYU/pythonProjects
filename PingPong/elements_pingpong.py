from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def paddle_creation(self, x, y):
        self.shape("square")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()


    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)


