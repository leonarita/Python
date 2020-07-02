from tkinter import *
from tkinter.ttk import *
from time import sleep

root = Tk()
progress1 = Progressbar(root, length=100)
progress1.pack()


def run():
    for x in range(101):
        progress1['value'] = x
        root.title(x)
        button1['text'] = x
        root.update_idletasks()
        sleep(.05)


button1 = Button(root, text="Load", command=run)
button1.pack()
root.mainloop()