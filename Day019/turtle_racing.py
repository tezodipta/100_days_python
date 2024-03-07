from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)
is_race = False
all_turtle = []

user_bet = screen.textinput("make your bet","which turtle will win the race choose a color:")
color_list = ["red","orange","yellow","blue","purple","green"]
y_position = [-70,-40,-10,20,50,80]

for index in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color_list[index])
    new_turtle.penup()
    new_turtle.goto(-230,y_position[index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the Winner")
                is_race = False 
            else:
                print(f"You've lost! The {winning_color} turtle is the Winner")
                is_race = False


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()