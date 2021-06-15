# Task 1 - heads or tails
import random
liczba = random.randint(0,1)
print('heads' if liczba == 0 else 'tails' )

# Task 2 - rand bill
names = input('Type names: ')
tab = names.strip().split(',')
print(f'For bill pays {random.choice(tab)}')

# Task 3 - treasure
row1 = ['😀','😀','😀']
row2 = ['😀','😀','😀']
row3 = ['😀','😀','😀']
mapa = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
pos = input('position: ')
col = int(pos[0]) - 1
row = int(pos[1]) - 1
mapa[row][col] = '😡'
print(f'{row1}\n{row2}\n{row3}')

# Task 4 - Rock / Paper / Sizors
pos = ['✊', '✋', '🤞']
print(['0', '1', '2'])
player1 = pos[int(input('Select option: '))]
# player1 = random.choice(pos)
print(player1)
player2 = random.choice(pos)
print(player2)
if(player1 == player2):
    print('draw')
elif(player1 == pos[0] and player2 == pos[2]):
    print('player1 win')
elif(player1 == pos[1] and player2 == pos[0]):
    print('player1 win')
elif(player1 == pos[2] and player2 == pos[1]):
    print('player1 win')
else:
    print('player2 win')