# Number Guessing Game!
import random

liczba = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

while True:
    dif = input("Choose a dificulty. Type 'easy' or hard: ")
    if dif == 'easy' or dif == 'hard':
        break
    else:
        print("I'm don't understend word, try again...")

max_attempts = 10 if dif == 'easy' else 5
attempts = 0
print(f'You have {max_attempts} attempts')

while True:
    # validacja liczby
    while True:
        try:
            guess = int(input('Make a guess: '))
            break
        except:
            print("Type a number, try again...")

    if guess > liczba:
        print('Too high.')
    elif guess < liczba:
        print('Too low.')
    else:
        print('You won!')
        break

    attempts += 1
    if attempts == max_attempts:
        print('You loose!')
        break
    else:
        print(f'You have {max_attempts - attempts} remaining to guess the number')
    
