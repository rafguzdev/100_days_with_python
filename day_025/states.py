import pandas
import turtle
from scoreboard import Scoreboard

screen = turtle.Screen()
scoreboard = Scoreboard()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')

score = 0
states = temp_list = data['state'].to_list()
xcor = temp_list = data['x'].to_list()
ycor = temp_list = data['y'].to_list()
while True:
    answer = screen.textinput(title=f'Guess the State {score}/50', prompt="What's another stat's name?")
    score += 1
    try:
        if answer == 'exit':
            break
        poz = states.index(answer)
        scoreboard.add(xcor[poz], ycor[poz], answer)
    except:
        print('Not found')

turtle.mainloop()