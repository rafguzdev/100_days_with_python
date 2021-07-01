from turtle import Screen, Turtle, heading, width
import time

screen = Screen()
screen.setup( width = 600, height = 600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

positions = [(0,0), (-20,0), (-40,0), (-60,0), (-80,0)]
snake = []
for idx, position in enumerate(positions):
    snake.append(Turtle())
    snake[idx].color('white')
    snake[idx].shape('square') 
    snake[idx].shapesize(1) 
    snake[idx].penup()
    snake[idx].goto(position)

def move_up():
    snake[0].setheading(90)

screen.update()
screen.listen()

screen.onkey(lambda : snake[0].setheading(90), 'w')
screen.onkey(lambda : snake[0].setheading(270), 's')
screen.onkey(lambda : snake[0].setheading(180), 'a')
screen.onkey(lambda : snake[0].setheading(0), 'd')


while True:
    cords = []
    for part in snake:
        cords.append((part.xcor(), part.ycor()))
           
    for idx, part in enumerate(snake):
        if idx > 0:
            part.goto(cords[idx-1])

    snake[0].fd(20)
    screen.update()
    time.sleep(0.1)






screen.exitonclick()