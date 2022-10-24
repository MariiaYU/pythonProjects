from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.new_speed = STARTING_MOVE_DISTANCE

    def move(self):

        for car in self.all_cars:
            car.backward(self.new_speed)

    def create(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_y = random.randint(-230, 230)
        new_car.goto(300, new_y)
        self.all_cars.append(new_car)

    def add_speed(self):
        self.new_speed += MOVE_INCREMENT












