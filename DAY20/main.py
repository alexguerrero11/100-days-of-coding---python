from turtle import Screen
from snake import Snake
import time

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initializing the snake
snake = Snake()

# Creating the snake body
snake.create_snake()

# Controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Moving the snake
game_active = True

while game_active:
    screen.update()
    time.sleep(0.1)  # delays the update
    # Snake takes the default steps forward
    snake.move_forward()

screen.exitonclick()
