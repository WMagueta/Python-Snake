from turtle import Screen
from snake import Snake
from food import Food
import time



screen = Screen()
screen.bgpic("assets/map.png")
screen.setup(width=410, height=410)
screen.title("Python Snake")
screen.tracer(0)

snake = Snake()
food = Food()

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
 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()


screen.exitonclick()