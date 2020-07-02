from tkinter import *
from tkinter.ttk import *
from time import strptime


def time():
    string = strptime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


root = Tk()
root.title("Clock")

lbl = Label(root, font=('lucidia', 40, 'bold'), background='red', foreground='white')
lbl.pack(anchor='center')
time()
mainloop()