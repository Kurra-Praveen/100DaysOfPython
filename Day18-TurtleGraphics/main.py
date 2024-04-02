import random
import turtle
from turtle import Turtle, Screen
import colorgram

timmy = Turtle()
screen = Screen()
turtle.colormode(255)
timmy.speed(0)
timmy.penup()
timmy.goto(-280, -210)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def drawDots():
    for i in range(12):
        timmy.dot(20, randomColor())
        timmy.forward(50)

def turnRight():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
def turnLeft():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.right(90)
for i in range(5):
    drawDots()
    turnRight()
    drawDots()
    timmy.dot(20,randomColor())
    turnLeft()



screen.exitonclick()
