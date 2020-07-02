import tkinter as tk
from tkinter.messagebox import showinfo


def convert():
    string = entry.get()
    inverted = string[::-1]
    showinfo("Word", f"{string} = {inverted}")


win = tk.Tk()

label = tk.Label(win, text="Enter string: ")
label.grid(row=0, column=0)

entry = tk.Entry(win, bg='#1DFD9B')
entry.grid(row=0, column=1, padx=10, pady=5)

button = tk.Button(win, text="INVERT", command=convert)
button.grid(row=1, column=0, columnspan=2)

win.mainloop()