from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.turtlesize(5,1)
        self.goto(pos)

    # game functions
    def goUp(self):
        posx = self.xcor()
        posy = self.ycor()
        self.goto(posx, posy+20)

    def goDown(self):
        posx = self.xcor()
        posy = self.ycor()
        self.goto(posx, posy-20)
