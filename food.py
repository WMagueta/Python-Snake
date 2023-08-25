from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-9, 9)
        y = random.randint(-9, 9)
        self.goto((x*20)-10, (y*20)-10)
