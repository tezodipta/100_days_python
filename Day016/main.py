from turtle import Turtle,Screen

#dont do it like this always create a object
# Turtle().shape("turtle")
my_turtle = Turtle()
my_turtle.color("red")
my_turtle.shape("turtle")
my_screen = Screen()
my_turtle.forward(100)

my_screen.exitonclick()