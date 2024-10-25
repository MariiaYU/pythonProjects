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
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def ball_to_another_player(self):
        self.home()
        self.x_move *= -1


class SeparateLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.setx(0)
        self.sety(300)
        self.goto(0, -300)
        self.goto(0, -70)
        self.circle(radius=70)





print("Hello")