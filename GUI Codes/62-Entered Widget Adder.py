from tkinter import *


def create():
    for x in range(init_val.get()):
        Entry(root).pack(pady=10)


root = Tk()
root.geometry("500x600")

Label(text="Enter the no of entry widget you want to create").pack()

init_val = IntVar()
init_ent = Entry(root, textvariable=init_val).pack()
Button(text="Create now", command=create).pack()

root.mainloop()