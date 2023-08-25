from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 180)
        self.color("orange")
        self.score = 0

    def update(self):
        self.clear()
        self.goto(0, 180)
        self.write(f"Score = {self.score}", False, "center", ("Arial", 14, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update()