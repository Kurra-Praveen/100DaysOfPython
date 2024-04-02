from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def goUp(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def doDown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
