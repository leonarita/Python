import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile


def open ():
    file = askopenfile(mode='r', filetypes=[('CSV File0', '*.csv')])
    content = pd.read_csv(file)
    data.insert(tk.END, content)


win = tk.Tk()
win.title("Load CSV File")

label = tk.Label(win, text="Select file")
label.grid(row=0, column=0, padx=8, pady=8)

button = tk.Button(win, text="Load", command=open)
button.grid(row=0, column=1, padx=8, pady=8)

data = tk.Text(win, height=10, widt=30)
data.grid(row=3, column=0, columnspan=2)

win.mainloop()