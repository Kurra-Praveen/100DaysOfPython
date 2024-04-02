from turtle import Screen
from Snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Welcome to snake game")
screen.tracer(0)
position = [(0, 0), (-20, 0), (-40, 0)]
listOfTurtles = []

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
isGameOn = True
while isGameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.detect_coll_wall():
        score.game_over()
        isGameOn = False

    if snake.detect_coll_tail():
        print("collision occurs")
        score.game_over()
        isGameOn = False


screen.exitonclick()
