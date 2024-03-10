from turtle import Screen,Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake =Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()


screen.exitonclick()