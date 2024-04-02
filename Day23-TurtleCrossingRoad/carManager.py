import random
from turtle import Turtle

COLORS = ["Red", "Green", "Yellow", "Orange", "Blue", "Brown", "Grey"]
STARTING_INCREMENT = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.allCars = []
        self.car_speed = STARTING_INCREMENT

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            y_axis = random.randint(-260, 260)
            new_car.goto(300, y_axis)
            self.allCars.append(new_car)

    def move_car(self):
        for car in self.allCars:
            car.backward(self.car_speed)

    def increase_carSpeed(self):
        self.car_speed += MOVE_INCREMENT
