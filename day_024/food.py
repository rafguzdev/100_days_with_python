import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5)
        self.color('red')
        self.speed('fastest')
        self.pos_x = random.randint(-280, 280)
        self.pos_y = random.randint(-280, 280)
        self.goto(self.pos_x, self.pos_y)
        
    def refresh(self):
        self.pos_x = random.randint(-280, 280)
        self.pos_y = random.randint(-280, 280)
        self.goto(self.pos_x, self.pos_y)