import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

win = tk.Tk()
win.title("Dropdown Menu")

var = tk.StringVar(win)
var.set("Fruits")

dropdown = tk.OptionMenu(win, var, "Apple", "Banana", "Watermelon", "Orange")
dropdown.pack()

win.mainloop()