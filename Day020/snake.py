from turtle import Turtle,Screen

SQUARE_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()   
    def create_snake(self):
        for position in SQUARE_POSITION:
            new_square = Turtle("square")
            new_square.penup()
            new_square.color("white")
            new_square.goto(position)
            self.squares.append(new_square)


    def move(self):
        for sqr_num in range(len(self.squares)-1,0,-1):
            new_x = self.squares[sqr_num-1].xcor()
            new_y = self.squares[sqr_num-1].ycor()
            self.squares[sqr_num].goto(new_x,new_y)
        self.squares[0].forward(MOVE_DISTANCE)
