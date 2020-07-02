from tkinter import *


def clicked():
    app.destroy()


app = Tk()

lab = Label(app, text="Write: ")
lab.grid(row=0, column=0)

en = Entry(app)
en.grid(row=0, column=1)

btn = Button(app, text='click here!', command=clicked)
btn.grid(row=1, columnspan=2)

app.mainloop()
