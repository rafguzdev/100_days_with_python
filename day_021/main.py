from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initialize window
screen = Screen()
screen.setup( width = 600, height = 600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

# initialize 
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# update screen after load all components2
screen.update()

# set keyboard actions
screen.listen()
screen.onkey(snake.move_up, 'w')
screen.onkey(snake.move_dw, 's')
screen.onkey(snake.move_lt, 'a')
screen.onkey(snake.move_rt, 'd')

# game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.go()

    # collisions
    if snake.head.distance(food) < 15:
        scoreboard.add()
        snake.grow()
        food.refresh()
    
    # detect collisions with wall
    if ( snake.head.xcor() > 300 or snake.head.xcor() < -300 or
        snake.head.ycor() > 300 or snake.head.ycor() < -300 ):
        game_is_on = False
        scoreboard.game_over()

    # detect collisions with tail
    for idx, segment in enumerate(snake.snake):
        if idx > 1:
            if snake.head.distance(segment) < 5:
                game_is_on = False
                scoreboard.game_over()
    

screen.exitonclick()
