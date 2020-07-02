from gtts import gTTS
import os
import tkinter as tk
from playsound import playsound
from tkinter import filedialog


def chooseFile():
    global content
    file = filedialog.askopenfile(filetypes=[('Text Files', '*.txt')])
    sFile = tk.Label(win, text=f"Selected File: {file.name}")
    sFile.grid(row=1, column=0, columnspan=2)
    if file is not None:
        content = file.read()
    return content


def convert():
    text = content
    speech = gTTS(text=content, lang="en")
    speech.save(r'C:\Teste\Python\speech.mp3')
    playsound(r'C:\Teste\Python\speech.mp3')


win = tk.Tk()

label = tk.Label(win, text='Select File')
label.grid(row=0, column=0, padx=8, pady=8)

button = tk.Button(win, text='Choose!', command=chooseFile)
button.grid(row=0, column=1, padx=8, pady=8)

button2 = tk.Button(win, text='Convert', command=convert)
button2.grid(row=2, column=0, padx=8, pady=8, columnspan=2)

win.mainloop()