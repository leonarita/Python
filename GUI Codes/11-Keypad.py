from tkinter import *

root = Tk()
root.title("Pad")

row1 = (1, 2, 3)
row2 = (4, 5, 6)
row3 = (7, 8, 9)
row4 = ("*", 0, "#")

for x, nol in enumerate(row1):
    button1 = Button(root, text=nol, activebackground="red")
    button1.grid(row=0, column=x)

for x, nol in enumerate(row2):
    button1 = Button(root, text=nol, activebackground="red")
    button1.grid(row=1, column=x)

for x, nol in enumerate(row3):
    button1 = Button(root, text=nol, activebackground="red")
    button1.grid(row=2, column=x)

for x, nol in enumerate(row4):
    button1 = Button(root, text=nol, activebackground="red")
    button1.grid(row=3, column=x)

root.mainloop()