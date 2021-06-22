# Black Jack
import random
cards = {
    'ace': 11,
    'king': 10,
    'quin': 10,
    'jack': 10,
    'ten': 10,
    'nine': 9,
    'eigth': 8,
    'seven': 7,
    'six': 6,
    'five': 5,
    'four': 4,
    'three': 3,
    'two': 2,
}
player_score = 0
computer_score = 0
fail = False

while not fail:
    card = random.choice(list(cards))
    if card == 'ace' and player_score > 10:
        player_score += 1
    else:
        player_score += cards[card]
    # player_score
    print(f'wylosowano {card}')
    print(f'obeczny wynik: {player_score}')
    
    if player_score > 21:
        print('przegrałeś - za duzo pkt')
        fail = True
        break

    if 'y' == input('Koniec? write "y" '):
        print('----------czas na komputer------------')
        break

while not fail:
    card = random.choice(list(cards))
    if card == 'ace' and computer_score > 10:
        computer_score += 1
    else:
        computer_score += cards[card]

    print(f'wylosowano {card}')
    print(f'obeczny wynik: {computer_score}')

    if computer_score > 21:
        print('wygrales!')
        break

    if computer_score > player_score:
        print('komputer - wygral')
        break

    