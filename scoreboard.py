from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score}", align="center", font=("Arial", 24, "normal"))
        self.goto(100, 250)
        self.write(f"{self.r_score}", align="center", font=("Arial", 24, "normal"))

    def left_score(self):
        self.l_score += 1
        self.score_update()

    def right_score(self):
        self.r_score += 1
        self.score_update()
