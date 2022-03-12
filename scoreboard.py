from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            high_score = int(file.read())
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score_counter()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.score_counter()

    def score_counter(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", move=False, align="center",
                   font=("ariel", 24, "normal"))

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
