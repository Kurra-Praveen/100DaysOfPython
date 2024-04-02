from turtle import  Screen
from paddels import Paddle
from ball import Ball
from scoreboard import Score
import time
POSITIONS = [(-360, 0), [360, 0]]

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle(POSITIONS[0])
right_paddle = Paddle(POSITIONS[1])
ball=Ball()
score=Score()

screen.listen()
screen.onkey(right_paddle.goUp, "Up")
screen.onkey(right_paddle.doDown, "Down")
screen.onkey(left_paddle.goUp, "w")
screen.onkey(left_paddle.doDown, "s")

isGameOn = True
while isGameOn:
     time.sleep(ball.move_speed)
     screen.update()
     ball.move()
     if ball.ycor()>280 or ball.ycor()<-280 :
          ball.bounce()
     if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
          ball.bounce_paddle()


     if ball.xcor()>380:

          score.inc_left_score()
          ball.resetBall()
     if ball.xcor()<-380:

          score.inc_right_score()
          ball.resetBall()


screen.exitonclick()
