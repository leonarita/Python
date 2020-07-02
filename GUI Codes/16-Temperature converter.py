from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title("Temperature Converter")
fonte = ('arial', 15, 'bold')


def c_to_f():
    value = int(entry.get())
    answer = (value * 9/5) + 32
    showinfo("Answer: ", f"{value}°C = {answer}°F")


def f_to_c():
    value = int(entry.get())
    answer = (value - 32) * 5/9
    showinfo("Answer: ", f"{value}°F = {answer}°C")


label = Label(win, text="Enter temperature here: ", font=fonte)
label.grid(row=0, columnspan=2)

entry = Entry(win, font=fonte)
entry.grid(row=1, columnspan=2)

button1 = Button(win, text="Calcius To Farnhite", font=fonte, command=c_to_f)
button1.grid(row=3, column=0)

button2 = Button(win, text="Farnhite To Calcius", font=fonte, command=f_to_c)
button2.grid(row=3, column=1)

win.mainloop()