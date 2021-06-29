from turtle import Screen, Turtle
from random import choice, randint
import turtle

tim = Turtle()
tim.shape('turtle')
tim.color('blue')
turtle.colormode(255)
tim.speed('fastest')
# tim.pensize(10)

# Task 1
# for i in range(7):
#     color = (randint(0, 255), randint(0, 255), randint(0, 255))
#     tim.pencolor(color)
#     angle = 360 / ( i + 3 )
#     for j in range(i+3):
#         tim.fd(100)
#         tim.right(angle)

# Task 2
# for _ in range(200):
#     color = (randint(0, 255), randint(0, 255), randint(0, 255))
#     tim.pencolor(color)
#     angle = choice([90, 180, 270, 360])
#     tim.setheading(angle)
#     tim.fd(20)

# Task 3
for _ in range(360):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    tim.pencolor(color)
    tim.circle(100)
    current_heading = tim.heading()
    tim.left(1)

tim.hideturtle()
screen = Screen()
screen.exitonclick()