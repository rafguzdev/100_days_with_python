from turtle import Turtle

POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.len = len(POSITIONS)
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for idx, position in enumerate(POSITIONS):
            self.snake.append(Turtle())
            self.snake[idx].color('white')
            self.snake[idx].shape('square') 
            self.snake[idx].shapesize(1) 
            self.snake[idx].penup()
            self.snake[idx].goto(position)
    
    def go(self):
        for seg_num in range(self.len -1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DIST)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def move_dw(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_lt(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_rt(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new = Turtle()
        new.color('white')
        new.shape('square') 
        new.shapesize(1) 
        new.penup()
        new.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        
        self.snake.append(new)
        self.len += 1