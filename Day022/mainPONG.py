from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle =Paddle((-350,0))
right_paddle =Paddle((350,0))
ball = Ball()


game_is_on = True

while True:
    screen.update()
    time.sleep(.05)
    screen.listen()
    screen.onkey(left_paddle.up,"w")
    screen.onkey(left_paddle.down,"s")
    screen.onkey(right_paddle.up,"Up")
    screen.onkey(right_paddle.down,"Down")
    ball.move()
    if ball.xcor < -300 or ball.xcor > 300 : 


screen.exitonclick()