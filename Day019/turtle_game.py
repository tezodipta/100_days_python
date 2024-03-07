from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def right_turn():
    tim.right(10)

def sprint():
    tim.forward(50)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()





screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(right_turn,"Right")
screen.onkey(sprint,"s")
screen.onkey(clear,"x")
screen.exitonclick()