import tkinter as tk
from tkinter.messagebox import showinfo, showerror, showwarning

win = tk.Tk()


def error():
    showerror("Error", "This is error box")


def info():
    showinfo("Info", "This is info box")


def warning():
    showwarning("Warning", "This is warning box")


button1 = tk.Button(win, text="Error", command=error).grid(row=0, column=0)
button2 = tk.Button(win, text="Info", command=info).grid(row=0, column=1)
button3 = tk.Button(win, text="Warning", command=warning).grid(row=0, column=2)

win.mainloop()
