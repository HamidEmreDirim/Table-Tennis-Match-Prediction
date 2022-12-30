from turtle import Turtle




class Border(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.setpos(-320, 270)
        self.pendown()
        self.pencolor("green")
        self.pensize(4)
        self.forward(640)
        self.right(90)
        self.forward(540)
        self.right(90)
        self.forward(640)
        self.right(90)
        self.forward(540)