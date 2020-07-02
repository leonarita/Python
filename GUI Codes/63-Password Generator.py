from tkinter import *
import pyperclip
import random


def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
             , 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '¨',
             '&', '*', '(', ')']

    p = ""

    for x in range(passlen.get()):
        p = p + random.choice(pass1)
    passstr.set(p)


def copytoclipboard():
    random_passwd = passstr.get()
    pyperclip.copy(random_passwd)


root = Tk()
root.geometry("400x400")

passstr = StringVar()
passlen = IntVar()
passlen.set(0)

Label(root, text="Password Generator Application", font="calibri 20 bold").pack()

Label(root, text="Enter password length").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generator Password", command=generate).pack(pady=7)

Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text="Copy to clipboard", command=copytoclipboard).pack(pady=7)

root.mainloop()