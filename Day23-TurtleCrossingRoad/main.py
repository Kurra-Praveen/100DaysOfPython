from turtle import Screen
from player import Player
from carManager import CarManager
from scordBoard import ScoraBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
car = CarManager()
score = ScoraBoard()
screen.onkey(player.move, "Up")
isGameOn = True
while isGameOn:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for cars in car.allCars:
        if cars.distance(player) < 20:
            score.game_over()
            isGameOn = False
    if player.is_at_finish_line():
        player.go_to_start()
        car.increase_carSpeed()
        score.increse_levelUp()
screen.exitonclick()
