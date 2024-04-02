import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput("Turtle race", "which color tutle win the race").title()
colors = ["Red", "Green", "Yellow", "Blue", "Purple"]
position = [-100, -50, 0, 50, 100, 150]

turtles = []
for i in range(0, 5):
    timmy = Turtle("turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x=-235, y=position[i])
    turtles.append(timmy)

style = ('Courier', 10, 'italic')
while True:
    currentTurtle = random.choice(turtles)
    if currentTurtle.xcor() > 230:
        winningColor = currentTurtle.pencolor()

        if winningColor == userBet:
            turtle.hideturtle()
            turtle.write('You Win!', font=style, align='center')
            turtle.hideturtle()
        else:
            turtle.write(f'you loose!{winningColor} turtle is the winner', font=style, align='center')
            turtle.hideturtle()
        break
    currentTurtle.forward(random.randint(1, 10))

screen.exitonclick()
