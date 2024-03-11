from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
screen.listen() 

snake =Snake()
food = Food()
score = Scoreboard()


screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for sqr in snake.squares[1:]:
        if snake.head.distance(sqr) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()