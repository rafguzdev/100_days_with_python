from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.x_pos = 0
        self.y_pos = 0
        self.x_dir = 10
        self.y_dir = 10
        
    def move(self):
        self.x_pos += self.x_dir
        self.y_pos += self.y_dir
        self.goto(self.x_pos, self.y_pos)  

    def bounce_y(self):
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1