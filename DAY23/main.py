import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating turtle for player
player = Player()

# Creating the scoreboard for the player
scoreboard = Scoreboard()

# Creating the car manager
car_manager = CarManager()

# Setting up screen to listen to the keystrokes to call this
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating and moving cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a perfect crossing
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.go_to_starting_position()
        car_manager.level_up()

screen.exitonclick()
