from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmov = 10
        self.ymov = 10

    def move(self):
        new_x = self.xcor() + 10 
        new_y = self.ycor() + 10 
        self.goto(new_x,new_y)

    def bounce(self):
        