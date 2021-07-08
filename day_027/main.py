import tkinter as tk
from tkinter import Button, Entry, Widget, font

window = tk.Tk()
window.title('GUI')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def calc():
    miles = int(entry.get())
    km = miles * 1.6
    exit_calc.config(text=str(km))

#declatations 
entry = tk.Entry(width=10)
entry_disc = tk.Label(text='Miles')

exit_disc = tk.Label(text='is equal to')
exit_calc = tk.Label(text='0')
exit_unit = tk.Label(text='Km')

button = tk.Button(text='Calculate', command=calc)

#positions 
entry.grid(column=1, row=0)
entry_disc.grid(column=2, row=0)

exit_disc.grid(column=0, row=1)
exit_calc.grid(column=1, row=1)
exit_unit.grid(column=2, row=1)

button.grid(column=1, row=2)

window.mainloop()