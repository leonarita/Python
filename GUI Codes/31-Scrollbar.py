import tkinter as tk

win = tk.Tk()

sc = tk.Scrollbar(win)
sc.pack(side="right", fill="y")

text = tk.Text(win, yscrollcommand=sc.set)
text.pack()

win.mainloop()