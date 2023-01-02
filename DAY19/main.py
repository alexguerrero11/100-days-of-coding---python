# Turtle Coordinate System
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [120, 70, 20, -30, -80, -130]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-200, y=y_position[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()