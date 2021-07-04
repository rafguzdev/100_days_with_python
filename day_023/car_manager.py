from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create(self):
        create = random.randint(1, 5)
        if create == 1:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.setheading(180)
            car.turtlesize(1,2)
            car.goto(300, random.randint(-200, 250))
            self.cars.append(car)

    def drive(self):
        for car in self.cars:
            car.fd(self.speed)

    def clear(self):
        for idx, car in enumerate(self.cars):
            if car.xcor() < -250:
                car.hideturtle()
                self.cars.pop(idx)

    def speedUp(self):
        self.speed += MOVE_INCREMENT