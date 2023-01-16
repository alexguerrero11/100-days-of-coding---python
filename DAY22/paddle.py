from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # set up shape
        self.color("white")  # set up color
        self.shapesize(stretch_len=1, stretch_wid=5)  # transforming into rectangle
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)