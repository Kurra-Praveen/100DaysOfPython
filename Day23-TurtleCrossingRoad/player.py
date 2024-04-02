from turtle import Turtle

STARTING_POSITION = (0, -280)
FORWARD = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(FORWARD)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

