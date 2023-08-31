from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 180)
        self.color("orange")
        self.score = 0
        self.high_score = 0

    def update(self):
        self.clear()
        self.goto(0, 175)
        self.write(f"Score = {self.score}", False, "center", ("Verdana", 16, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update()

    def gameover(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
        self.goto(0, -27)
        self.write(f"   Game Over\n High Score = {self.high_score}", False, "center", ("Verdana", 28, "normal"))
