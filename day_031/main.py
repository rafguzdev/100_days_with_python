from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
pick = []
original_data = {}

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# load data from file
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict('records')
else:
    to_learn = data.to_dict('records')


def next_card():
    global pick, flip_timer
    window.after_cancel(flip_timer)
    pick = random.choice(to_learn)
    print(pick)
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfigure(title, text='French')
    canvas.itemconfigure(word, text=pick['French'])
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfigure(title, text='English')
    canvas.itemconfigure(word, text=pick['English'])


def is_known():
    to_learn.remove(pick)
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# view
canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, 'italic'))
word = canvas.create_text(400, 263, text='word', font=("Ariel", 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
r_img_button = PhotoImage(file='images/right.png')
r_button = Button(image=r_img_button, highlightthickness=0, command=is_known)
w_img_button = PhotoImage(file='images/wrong.png')
w_button = Button(image=w_img_button, highlightthickness=0, command=next_card)
w_button.grid(row=1, column=0)
r_button.grid(row=1, column=1)
flip_timer = window.after(3000, flip_card)
next_card()


window.mainloop()
