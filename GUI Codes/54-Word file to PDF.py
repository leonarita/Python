import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo


def openFile():
    file = askopenfile(filetypes=[('Word Files', '*.docx')])
    convert(file.name, r'C:\Teste\Python\converted.pdf')
    showinfo("Done", "File successfully converted")


win = tk.Tk()
win.title("Word To PDF Converter")

label = tk.Label(win, text="Choose file: ")
label.grid(row=0, column=0, padx=5, pady=5)

button = ttk.Button(win, text="Select", width=30, command=openFile)
button.grid(row=0, column=1, padx=5, pady=5)

win.mainloop()