from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmov = 10
        self.ymov = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmov
        new_y = self.ycor() + self.ymov 
        self.goto(new_x,new_y)

    def x_bounce(self):
        self.xmov *= -1
        self.ball_speed *= 0.9

    def y_bounce(self):
        self.ymov *= -1

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.x_bounce()
        