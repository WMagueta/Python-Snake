from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 180)
        self.color("orange")
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = data.read()
            self.high_score = int(self.high_score)

    def update(self):
        self.clear()
        self.goto(0, 175)
        self.write(f"Score = {self.score}", False, "center", ("Verdana", 14, "normal"))
        self.goto(0, 150)
        self.write(f"High Score = {self.high_score}", False, "center", ("Verdana", 14, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update()

    def gameover(self):
        with open("data.txt", "r") as data:
            if self.score > int(data.read()):
                with open("data.txt", "w") as uptading_data:
                    self.high_score = self.score
                    uptading_data.write(str(self.high_score))
        self.score = 0
        self.update()
        self.goto(0, -27)
        self.write(f"Game Over", False, "center", ("Verdana", 16, "normal"))
