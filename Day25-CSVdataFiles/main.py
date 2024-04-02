from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
# screen.setup(width=900,height=650)
path="./indiaMap.gif"
screen.addshape(path)
timmy.shape(path)

user_guess=screen.textinput("make a guess","guess the state name")

screen.mainloop()
