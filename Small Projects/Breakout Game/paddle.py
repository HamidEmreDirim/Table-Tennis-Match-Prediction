from turtle import Turtle




class Paddle(Turtle):

    def __init__(self) :
        super().__init__()
    
        self.color("white")
        self.shape("square")
        self.shapesize(0.5, 5)
        self.penup()
        self.goto(x=0, y=-100)
        self.MOVE_DISTANCE_R = 30
        self.MOVE_DISTANCE_L = 30
    

    def right(self):
            
        self.forward(self.MOVE_DISTANCE_R)

    def left(self):

            self.backward(self.MOVE_DISTANCE_L)

    def border_r(self):

        self.MOVE_DISTANCE_R = 0

    def border_l(self):

        self.MOVE_DISTANCE_L = 0
    
    def n_l(self):

        self.MOVE_DISTANCE_L = 30
    
    def n_r(self):

        self.MOVE_DISTANCE_R = 30

        

        
    