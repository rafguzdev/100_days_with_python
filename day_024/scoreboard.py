from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hiscore = self.load_hiscore()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}  High Score: {self.hiscore}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align='center', font=('Arial', 14, 'normal'))

    def add(self):
        self.score += 1
        if self.score > self.hiscore:
            self.hiscore = self.score
            self.write_hiscore()
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.hiscore}", align='center', font=('Arial', 24, 'normal'))

    def load_hiscore(self):
        score = 0
        with open('score.txt') as file:
            score = int(file.read())
        return score

    def write_hiscore(self):
        file = open('score.txt', 'w')
        file.write(str(self.hiscore))
        file.close()