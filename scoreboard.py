from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.draw_net()

        self.setpos(0, 250)
        self.write(f"{self.left_score}     {self.right_score}", False, align="center", font=('Courier', 30, 'bold'))

    def draw_net(self):
        self.penup()
        self.setpos(0, 300)
        self.setheading(270)
        for _ in range(0, 15):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(30)

    def score_left(self):
        self.left_score += 1
        self.update_scoreboard()

    def score_right(self):
        self.right_score += 1
        self.update_scoreboard()
