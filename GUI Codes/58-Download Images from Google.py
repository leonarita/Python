import requests
import shutil
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo


def download():
    url = entry.get()
    img = requests.get(url, stream=True)
    saveImg = open(r'C:\Teste\Python\img.png', 'wb')
    shutil.copyfileobj(img.raw, saveImg)
    showinfo("Done", "Image downloaded successfully")


win = tk.Tk()
win.title("Image Downloader")

label = tk.Label(win, text="Enter URL here: ")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(win, width=30)
entry.grid(row=0, column=1, padx=5, pady=5)

button = ttk.Button(win, text="Download", command=download)
button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

win.mainloop()


