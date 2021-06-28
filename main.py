from turtle import Screen, Turtle
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()

#paddle class
#ball class
#score class (with divide line)

#create screen
#create paddles
#move paddles with user input
#create ball
#move ball
#change ball direction if contact with top/bottom screen or paddle
#create score
#update score if ball goes off screen
#reset game state
#end game once score reached