from turtle import *
turtle = Turtle()
def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def dash(size,inp_range):
    for i in range(inp_range):
        turtle.forward(size)
        turtle.penup()
        turtle.forward(size)
        turtle.pendown()

# square(200)
dash(10,15)
screen = Screen()
screen.exitonclick()