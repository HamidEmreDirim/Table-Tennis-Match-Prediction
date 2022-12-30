from turtle import Turtle




class Brick():

    def __init__(self):
        self.segments = []

    def add_brick(self, color, shapesizey, shapesizex, xloc, yloc):
        new_brick = Turtle("square")
        new_brick.color(color)
        new_brick.shapesize(shapesizey, shapesizex)
        new_brick.penup()
        new_brick.goto(x=xloc, y=yloc)
        self.segments.append(new_brick)

        
        
        