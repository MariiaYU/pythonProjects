from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
colormode(255)
color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205), (204, 119, 35), (112, 6, 4)]
timmy.speed(0)
y=-300
while y!=350:
    timmy.penup()
    timmy.goto(-300, y)
    timmy.pendown()
    for _ in range(13):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    y += 50



screen = Screen()
screen.exitonclick()





# import colorgram

# def colors_from_image(image_name):
#     """Create a list of colors from added image"""
#     colors = colorgram.extract(image_name, 30)
#     list = []
#     for x in range(0, 30):
#         first_color = colors[x]
#         list.append((first_color.rgb.r, first_color.rgb.g, first_color.rgb.b))
#     return list
#
# print(colors_from_image('image.jpg'))


