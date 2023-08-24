from turtle import Screen, Turtle
from snake import Snake
import time
import random

#screen configuration
screen = Screen()
screen.bgpic("assets/map.png")
screen.setup(width=810, height=810)
screen.title("Python Snake")
screen.tracer(0)

snake = Snake()

screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()