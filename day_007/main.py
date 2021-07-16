# Hangman
import random
word_list = ['ardvark', 'baboon', 'camel']
rand_word = random.choice(word_list)
hide_word = []
for letter in rand_word:
    hide_word.append('_')

while True:
    user_letter = input('type a leter: ')
    for idx, letter in enumerate(rand_word):
        if letter == user_letter:
            hide_word[idx] = letter
    print(hide_word)
    if '_' not in hide_word:
        print('you win')
        break
