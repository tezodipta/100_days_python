from turtle import Turtle,Screen

#dont do it like this always create a object
# Turtle().shape("turtle")
# my_turtle = Turtle()
# my_turtle.color("red")
# my_turtle.shape("turtle")
# my_screen = Screen()
# my_turtle.forward(100)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon name",["pikachu","squirtle","charmander"])
table.add_column("type",["electric","water","fire"])
table.align = "l"
#either we can use table.align or we can put any align argument in add_column

print(table)