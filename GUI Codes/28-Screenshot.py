import tkinter as tk
import pyautogui

win = tk.Tk()
win.title("Take Screenshot")
win.geometry('300x300')


def takescreenshot():
    screen = pyautogui.screenshot()
    screen.save('screenshot.png')


button = tk.Button(win, text='Capture screenshot', command=takescreenshot)
button.pack()

win.mainloop()