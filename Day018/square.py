from turtle import *
import turtle as t
import random

color = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
t.colormode(255)
turtle = Turtle()

# turtle.pensize(10)
turtle.speed("fastest")


def random_color():
    """this function will generate a random color"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def square(size):
    """this function will draw a square with the given size"""
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def dash(size,inp_range):
    """this function will draw a dashed line with the given size and range"""
    for i in range(inp_range):
        turtle.forward(size)
        turtle.penup()
        turtle.forward(size)
        turtle.pendown()


def shape(shape):
    """this function will draw a shape with the given number of size """
    num_side = 3
    for i in range(shape):
        turtle.color(random.choice(color))
        for j in range(num_side):
            angle = 360/num_side
            turtle.forward(100)
            turtle.right(angle)
        num_side += 1

def random_walk(steps):
    """this function will draw a random walk with the given number of steps"""
    for i in range(steps):
        turtle.color(random_color())
        turtle.forward(30)
        turtle.setheading(random.choice([0,90,180,270]))

def draw_sporograph(size_of_gap):
    """this function will draw a sporograph """
    for i in range(int(360/size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


# square(200)
# dash(10,15)
# shape(8)
# random_walk(100) 
# draw_sporograph(5)
screen = Screen()
screen.exitonclick()