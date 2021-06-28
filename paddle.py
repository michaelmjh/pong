from turtle import Turtle

START_POSITIONS = [(-350, 0), (350, 0)]
PADDLES = []

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setpos(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -260:
            self.goto(self.xcor(), new_y)
