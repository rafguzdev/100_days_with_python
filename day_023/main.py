import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move , 'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create()
    carManager.drive()
    carManager.clear()

    # detect collisions
    for car in carManager.cars:
        if player.distance(car) < 19:
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor() > 250:
        scoreboard.add()
        player.newRound()
        carManager.speedUp()
    
screen.exitonclick()
