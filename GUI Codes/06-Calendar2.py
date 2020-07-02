from tkinter import *
import calendar

root = Tk()
root.title("Calendar")
root.geometry("260x200")


def show():
    a = spin1.get()
    b = spin2.get()
    a = int(a)
    b = int(b)
    cal = calendar.month(b, a)
    text.delete(0.0, END)
    text.insert(INSERT, cal)


spin1 = Spinbox(root, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width=4)
spin1.place(x=20, y=0)

spin2 = Spinbox(root, from_=1878, to=2100, width=4)
spin2.place(x=80, y=0)

button = Button(root, text="GO", command=show)
button.place(x=140, y=0)

text = Text(root, width=24, height=8)
text.place(x=20, y=40)

root.mainloop()