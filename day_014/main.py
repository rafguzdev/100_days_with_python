# Higher lower Game
import random
from game_data import data
import art
import os

clear = lambda: os.system('cls')

print(art.logo)
score = 0
# print(data)
while True:
    choices = random.choices(data, k=2)
    print(f'Cpmpare A: {choices[0]["name"]}, a {choices[0]["description"]}, form {choices[0]["country"]}')
    print(art.vs)
    print(f'Against B: {choices[1]["name"]}, a {choices[1]["description"]}, form {choices[1]["country"]}')
    choice = input('Who has more followers? Type "A" or "B": ').lower()
    if ( choice == 'a' and choices[0]["follower_count"] < choices[1]["follower_count"] or
    choice == 'b' and choices[1]["follower_count"] < choices[0]["follower_count"] ):
        score += 1
        clear()
        print(art.logo)
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score {score}")
        break

