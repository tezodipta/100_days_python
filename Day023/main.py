import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
new_car = CarManager()
scoreboard = Scoreboard() 

screen.listen()
screen.onkeypress(player.go_up,"Up")
screen.onkeypress(player.go_down,"Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car.create_cars()
    new_car.move_cars()

    #detect collision with car
    for car in new_car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detact successful crossing
    if player.ycor() > 280:
        player.goto(0, -280)
        new_car.level_up()
        scoreboard.increase_level()
        

screen.exitonclick()

