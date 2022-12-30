from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = -20
        self.shape("circle")
        self.left(90)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.goto(self.x, self.y)
        self.x_move = random.uniform(-2.0, 2.0)
        self.y_move = -2.0
    
    def move(self, bonus=0):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        

