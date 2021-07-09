from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
sign = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    title.config(text='Timer', fg=GREEN)
    cancas.itemconfig(timer_text, text=f'00:00')
    window.after_cancel(timer)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minutes =  count / 60
    seconds = count % 60
    minutes = math.floor(minutes)

    if seconds < 10:
        seconds = f'0{seconds}'
    if minutes < 10:
        minutes = f'0{minutes}'

    cancas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global sign
    reps += 1

    if reps in [1, 3, 5, 7]:
        count_down(60 * WORK_MIN)
        title.config(text='Study', fg=GREEN)
    elif reps in [2, 4, 6]:
        count_down(60 * SHORT_BREAK_MIN)
        title.config(text='Break', fg=PINK)
    else:
        count_down(60 * LONG_BREAK_MIN)
        title.config(text='Break', fg=RED)
        reps = 0
        sign += '✓'
        mark.config(text=sign)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

cancas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato_img = PhotoImage(file='tomato.png')
cancas.create_image(100, 112, image=tomato_img)
timer_text = cancas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
cancas.grid(row=1, column=1)

title = Label(text='Timer', font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
title.grid(row=0, column=1)
btnStart = Button(text='Start', command=start_timer)
btnStart.grid(row=2, column=0)
btnReset = Button(text='Reset', command=reset_timer)
btnReset.grid(row=2, column=2)
mark = Label(text='', font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
mark.grid(row=3, column=1)

window.mainloop()