from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
colormode(255)

def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.speed(0)

def size_of_gap(size):
    for _ in range(int(360/size)):
        timmy.color(color())
        timmy.circle(100)
        timmy.seth(timmy.heading()+size)

size_of_gap(20)


# angle = [0, 90, 180, 270]
# on=True
# while on:
#     timmy.color(color())
#     x = random.choice(angle)
#     timmy.seth(x)
#     timmy.forward(30)





# x=3
# y=True
# for tyt in range(8):
#     col=random.choice(color)
#     timmy.color(col)
#     corner=360/x
#     for _ in range(x):
#         timmy.forward(100)
#         timmy.right(corner)
#     x+=1
