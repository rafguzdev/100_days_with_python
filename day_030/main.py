from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def save():

    website = e_website.get()
    email = e_email_user.get()
    password = e_password.get()

    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror('Error', 'Empty fields!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These aew the details entered: \nEmail: {email}'
                                                    f'\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            try:
                with open('file.json', 'r') as f:
                    data = json.load(f)
                    data.update(new_data)
            except FileNotFoundError:
                    data = new_data
            finally:
                with open('file.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    e_website.delete(0, END)
                    e_password.delete(0, END)

def generate():
    password = []
    for _ in range(5):
        password.append(random.choice(letters))
        password.append(random.choice(numbers))
        password.append(random.choice(symbols))
    random.shuffle(password)
    password = ''.join(password)
    e_password.delete(0, END)
    e_password.insert(0, password)
    pyperclip.copy(password)

def search():
    try:
        with open('file.json', 'r') as f:
            data = json.load(f)
            website = e_website.get()
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f'Email: {email} \nPassword: {password}')
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title=website, message='Not found.')
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='File not found.')

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# logo
cancas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
cancas.create_image(100, 100, image=logo)
cancas.grid(row=0, column=1)

# labels
l_website = Label(text='Website:')
l_website.grid(row=1, column=0)
l_email_user = Label(text='Email/User:')
l_email_user.grid(row=2, column=0)
l_password = Label(text='Password:')
l_password.grid(row=3, column=0)

# inputs
e_website = Entry(width=50)
e_website.grid(row=1, column=1, columnspan=2)
e_website.focus()
e_email_user = Entry(width=50)
e_email_user.insert(0, 'rafal@gmail.com')
e_email_user.grid(row=2, column=1, columnspan=2)
e_password = Entry(width=50)
e_password.grid(row=3, column=1, columnspan=2)

# buttons
b_gen = Button(text='Generate', width=42, command=generate)
b_gen.grid(row=4, column=1, columnspan=2)
b_add = Button(text='Add', width=42, command=save)
b_add.grid(row=5, column=1, columnspan=2)
b_search = Button(text='Search', width=42, command=search)
b_search.grid(row=6, column=1, columnspan=2)

window.mainloop() 