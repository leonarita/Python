import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

win = tk.Tk()
win.title("Random Number Generator")


def play():
    random_numer = random.randint(0, 6)
    number.config (text=f'Number is: {random_numer}')

    if random_numer == 0:
        showinfo("Congratulations", "YOU WON!!!")


number = ttk.Label(win, text="")
number.pack(pady=10)

play = ttk.Button (win, text="Play", command=play)
play.pack(padx=50)

win.mainloop()