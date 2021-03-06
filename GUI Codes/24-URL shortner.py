import pyshorteners
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("URL Shortener")


def short():
    url = entry_url.get()
    shorted_url = pyshorteners.Shortener()
    showinfo("Shorted URL", f"{shorted_url.tinyurl.short(url)}")


url_label = tk.Label(win, text="Entry URL here: ")
url_label.grid(row=0, column=0)

entry_url = tk.Entry(win, width=30, bg="#69BEF6", bd=2)
entry_url.grid(row=0, column=1, padx=5, pady=5)

button = tk.Button(win, text="Short", command=short)
button.grid(row=1, column=0, columnspan=2)

win.mainloop()