import numpy as np
import tkinter as tk
import tkinter.ttk as ttk


def multiply():
    a = entry1.get()
    a = list(map(int, a))

    b = entry2.get()
    b = list(map(int, b))

    c = entry3.get()
    c = list(map(int, c))

    d = entry4.get()
    d = list(map(int, d))

    e = entry5.get()
    e = list(map(int, e))

    x = np.array((a, b))
    y = np.array((c, d, e))
    z = np.dot(x, y)
    print(z)


win = tk.Tk()
win.title("2x3 Matrix Solver")

label1 = tk.Label(win, text="Enter 1st row of Matrix X: ")
label1.grid(row=0, column=0, padx=8, pady=8)

entry1 = tk.Entry(win, bg="#1DFD9B")
entry1.grid(row=0, column=1, padx=8, pady=8)

label2 = tk.Label(win, text="Enter 2st row of Matrix X: ")
label2.grid(row=1, column=0, padx=8, pady=8)

entry2 = tk.Entry(win, bg="#1DFD9B")
entry2.grid(row=1, column=1, padx=8, pady=8)

label3 = tk.Label(win, text="Enter 1st row of Matrix Y: ")
label3.grid(row=2, column=0, padx=8, pady=8)

entry3 = tk.Entry(win, bg="#1DFD9B")
entry3.grid(row=2, column=1, padx=8, pady=8)

label4 = tk.Label(win, text="Enter 2st row of Matrix Y: ")
label4.grid(row=3, column=0, padx=8, pady=8)

entry4 = tk.Entry(win, bg="#1DFD9B")
entry4.grid(row=3, column=1, padx=8, pady=8)

label5 = tk.Label(win, text="Enter 3st row of Matrix Y: ")
label5.grid(row=4, column=0, padx=8, pady=8)

entry5 = tk.Entry(win, bg="#1DFD9B")
entry5.grid(row=4, column=1, padx=8, pady=8)

button = tk.Button(win, text="Calculate", command=multiply)
button.grid(row=5, column=0, columnspan=2, padx=8, pady=8)

win.mainloop()