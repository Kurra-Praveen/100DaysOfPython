from turtle import Turtle

ALIGN = "Center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = self.retrive_high_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScoreText()

    def updateScoreText(self):
        self.update_score()
        self.write(f"Score={self.score}        High score={self.highScore}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.updateScoreText()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over !!", align=ALIGN, font=FONT)

    def retrive_high_score(self):
        with open("high_score.txt") as file:
            current_high_score = int(file.read())
            return current_high_score

    def update_score(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.score}")
