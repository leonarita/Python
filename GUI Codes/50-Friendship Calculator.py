import random
import tkinter as tk
import pandas as pd
import datetime


def check():
    global result
    text_area = tk.Text(master=root, height=2, width=60, bg="#FFFF99")
    text_area.grid(column=0, row=5)
    result = ("Friendship score is: ", result)
    text_area.insert(tk.END, result)


root = tk.Tk()
root.geometry("400x300")
root.title("Friendship Calculator")
result = 40 + int(pd.datetime.now().second)

# entry1 = tk.Entry(root, width=20, textvariable=name1)
entry1 = tk.Entry(root, width=20)
entry1.grid(column=1, row=1)

# entry2 = tk.Entry(root, width=20, textvariable=name2)
entry2 = tk.Entry(root, width=20)
entry2.grid(column=1, row=2)

button1 = tk.Button(text="CHECK LOVE", bg="pink", command=check)
button1.grid(column=1, row=3)

label1 = tk.Label(root, text='Your name: ', bg='red', font=('', 15, 'bold'))
label1.grid(row=1, column=0, pady=5, padx=5)

label2 = tk.Label(root, text='Friend name: ', bg='red', font=('', 15, 'bold'))
label2.grid(row=2, column=0, pady=5, padx=5)

root.mainloop()