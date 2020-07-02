from tkinter import *


def open_window():
    top = Toplevel()
    top.title("top window")
    top.geometry("200x100")
    button1 = Button(top, text="close", command=top.destroy)
    button1.pack()


root = Tk()
button = Button(root, text="open window", command=open_window)
button.pack()

root.geometry("200x100")
root.mainloop()