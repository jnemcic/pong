from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.color("white")

    def move_up(self):
        self.penup()
        new_y = self.ycor() + 20
        if new_y < 260:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        self.penup()
        new_y = self.ycor() - 20
        if new_y > -260:
            self.goto(self.xcor(), new_y)
