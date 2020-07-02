import tkinter as tk

win = tk.Tk()
win.title("Radio Button")

var = tk.IntVar()

value1 = tk.Radiobutton(win, text="EUA", value=1, variable=var).pack()
value2 = tk.Radiobutton(win, text="China", value=2, variable=var).pack()
value3 = tk.Radiobutton(win, text="Russia", value=3, variable=var).pack()

win.mainloop()

if __name__ == '__main__':
    win
