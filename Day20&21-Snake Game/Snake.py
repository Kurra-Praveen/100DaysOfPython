import turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.listOfTurtles = []
        self.crateSnake()
        self.head = self.listOfTurtles[0]

    def crateSnake(self):
        for eachPosition in POSITION:
            self.add_snake(eachPosition)

    def add_snake(self, eachPosition):
        timmy = turtle.Turtle(shape="square")
        timmy.penup()
        timmy.color("white")
        timmy.setpos(eachPosition)
        self.listOfTurtles.append(timmy)

    def extend(self):
        self.add_snake(self.listOfTurtles[-1].position())

    def move(self):
        for seg in range(len(self.listOfTurtles) - 1, 0, -1):
            xcor = self.listOfTurtles[seg - 1].xcor()
            ycor = self.listOfTurtles[seg - 1].ycor()
            self.listOfTurtles[seg].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def xcor(self):
        return self.head.xcor()

    def ycor(self):
        return self.head.ycor()

    def detect_coll_wall(self, ):
        if self.xcor() > 290 or self.xcor() < -290 or self.ycor() > 290 or self.ycor() < -290:
            return True
        return False

    def detect_coll_tail(self):
        for eachSnake in self.listOfTurtles[1:]:
            if self.head.distance(eachSnake) < 10:
                return True
        return False
