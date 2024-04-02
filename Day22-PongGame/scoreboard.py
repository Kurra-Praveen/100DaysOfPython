from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.displayScore()

    def displayScore(self):
        self.clear()
        self.goto(-130, 200)
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))
        self.goto(130, 200)
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    def inc_left_score(self):

        self.l_score += 1
        self.displayScore()

    def inc_right_score(self):
        self.r_score += 1
        self.displayScore()
