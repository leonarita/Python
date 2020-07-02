import tkinter as tk
from tkinter import filedialog
from PIL import Image


def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    im1.save(export_file_path)


root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

browseButton_PNG = tk.Button(text="Image PNG File", command=getPNG, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)

saveAsButton_PNG = tk.Button(text="Convert PNG to JPG", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_PNG)

root.mainloop()