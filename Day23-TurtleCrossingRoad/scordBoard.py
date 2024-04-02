from turtle import Turtle

FONT = ("arial", 30, "normal")


class ScoraBoard(Turtle):
    def __init__(self):
        super(ScoraBoard, self).__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.increse_levelUp()

    def increse_levelUp(self):
        self.clear()
        self.level += 1
        self.write(f"level :{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
