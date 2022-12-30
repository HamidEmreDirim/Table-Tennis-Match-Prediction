from turtle import Screen
import turtle
from brick import Brick
from border import Border
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=620)
screen.title("Pong")
screen.bgcolor("black")

screen.tracer(0)

game_line = Border()


brick = Brick()
scoreboard = Scoreboard()



def block_brick(redy = 250):
    redx = -250
    

    v_space= 18



    
    for i in range(6):

        if i < 4: 
            brick.add_brick(color="red", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy)
            brick.add_brick(color="yellow", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - v_space)
            brick.add_brick(color="purple", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - 2 *v_space)
            redx += 35
            brick.add_brick(color="red", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy)
            brick.add_brick(color="yellow", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - v_space,)
            brick.add_brick(color="purple", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - 2*v_space)
            redx += 43

            

        else:
            brick.add_brick(color="red", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy)
            brick.add_brick(color="yellow", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - v_space)
            brick.add_brick(color="purple", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - 2*v_space)
            redx += 35
            brick.add_brick(color="red", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy)
            brick.add_brick(color="yellow", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - v_space)
            brick.add_brick(color="purple", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - 2*v_space)
            redx += 35
            brick.add_brick(color="red", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy)
            brick.add_brick(color="yellow", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - v_space)
            brick.add_brick(color="purple", shapesizex = 1.5, shapesizey=0.6, xloc=redx, yloc=redy - 2*v_space)
            redx += 43
        
block_brick()
block_brick(redy= 196)
block_brick(redy= 142)
block_brick(redy=88)

paddle = Paddle()
ball = Ball()

screen.listen()



screen.onkeypress(paddle.left, "Left")
    
screen.onkeypress(paddle.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    

    if paddle.xcor() > 250:
        paddle.border_r()  
    else:
        paddle.n_r()

    if paddle.xcor() < -250:
        paddle.border_l()

    else:
        paddle.n_l()

    ball.move()

    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    if ball.xcor() > 310 or ball.xcor() < -310:
        ball.bounce_x()
    
    if ball.distance(paddle) < 40:
        ball.bounce_y()
        ball.move()
        ball.move()
        ball.move()
        ball.move()
        ball.move()
        
        

    for b in brick.segments:

        if ball.distance(b) < 20 :
            if (ball.towards(b) >= 45 and ball.towards(b) <= 135) or (ball.towards(b) >= 225 and ball.towards(b) <= 315):
                ball.bounce_y()
                b.reset()           
                ball.move()
                ball.move()
                scoreboard.increase_score()
            else:
                ball.bounce_x()
                b.reset()           
                ball.move()
                ball.move()
                scoreboard.increase_score()
    
    if ball.ycor() < -120:
        ball.reset()
        scoreboard.game_over()
        game_is_on = False

        

        


            
    
    
    



    





    


    




screen.exitonclick()