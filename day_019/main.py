from turtle import Screen, Shape, Turtle, speed
import random


turtles = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-70, -40, -10, 20, 50, 80]
for idx, color in enumerate(colors):
    turtles.append(Turtle(shape='turtle'))
    turtles[idx].color(color)
    turtles[idx].penup()
    turtles[idx].goto(-220, y_pos[idx])

screen = Screen()
screen.setup(width = 500, height = 400)
color = screen.textinput("Bet", 'Choose your turtle by color')
win = 'NULL'

def move_fd():
    for idx in range(6):
        speed = random.randint(0,10)
        turtles[idx].fd(speed)

def check_pos():
    for idx in range(6):
        if turtles[idx].xcor() > 220:
            print(f'Winner is {turtles[idx].fillcolor()}')
            if color == turtles[idx].fillcolor():
                print("You've won!")
            else:
                print("You've lost!")
            return True
            
race_on = True
while race_on:
    move_fd()
    if check_pos():
        break

screen.listen()
screen.onkey(move_fd, 'w')

screen.exitonclick()
