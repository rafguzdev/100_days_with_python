from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# initialize window
screen = Screen()
screen.setup( width = 800, height = 600)
screen.bgcolor('black')
screen.title('My pong game')
screen.tracer(0)

# players
l_paddle = Paddle((-350, 0))
r_paddle = Paddle(( 350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(l_paddle.goUp , 'w')
screen.onkey(l_paddle.goDown , 's')
screen.onkey(r_paddle.goUp , 'Up')
screen.onkey(r_paddle.goDown , 'Down')

# game loop
game_is_on = True
while game_is_on:
    ball.move()
    screen.update()

    # bounce walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce paddle
    if ball.xcor() >= 330:
        if ball.distance(r_paddle) < 50:
            ball.bounce_x()
            scoreboard.add()
        else:
            game_is_on = False
            scoreboard.game_over()
    if ball.xcor() <= -330:
        if ball.distance(l_paddle) < 50:
            ball.bounce_x()
            scoreboard.add()
        else:
            game_is_on = False
            scoreboard.game_over()
    
    time.sleep(0.05)
    # snake.go()



screen.exitonclick()