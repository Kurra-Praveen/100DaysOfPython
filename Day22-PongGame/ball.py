from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("violet")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.ymove
        new_x = self.xcor() + self.xmove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1

    def bounce_paddle(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def resetBall(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_paddle()
