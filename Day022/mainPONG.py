from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle =Paddle((-350,0))
right_paddle =Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    screen.listen()
    screen.onkeypress(left_paddle.up,"w")
    screen.onkeypress(left_paddle.down,"s")
    screen.onkeypress(right_paddle.up,"Up")
    screen.onkeypress(right_paddle.down,"Down")
    ball.move()
    
    if ball.ycor() < -280 or ball.ycor() > 280 :
        ball.y_bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340 : 
        ball.x_bounce()

    #detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position() 
        scoreboard.l_point()

    #for the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score > 10 or scoreboard.r_score > 10:
        game_is_on = False



screen.exitonclick()