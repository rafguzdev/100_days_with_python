from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color('black')
        self.hideturtle()
        self.penup()

    def add(self,posx, posy, state):
        self.goto(posx, posy)
        self.write(state, align='center', font=FONT)


