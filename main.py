from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    if ball.xcor() > 420:
        ball.reset_ball()
        scoreboard.score_left()

    if ball.xcor() < -420:
        ball.reset_ball()
        scoreboard.score_right()

screen.exitonclick()
