import datetime
import tkinter as tk
from PIL import Image, ImageTk


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        return age


def getInput():
    name = nameEntry.get()
    monkey = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = "Heyy {monkey}!!! You are {age} years old".format(monkey=name, age=monkey.age())
    textArea.insert(tk.END, answer)


window = tk.Tk()
window.geometry("620x780")
window.title("Age Calculator App")

name = tk.Label(text="Name")
name.grid(column=0, row=1)

year = tk.Label(text="Year")
year.grid(column=0, row=2)

month = tk.Label(text="Month")
month.grid(column=0, row=3)

date = tk.Label(text="Day")
date.grid(column=0, row=4)

nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)

yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)

monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)

dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)

button = tk.Button(window, text="Calculate Age", command=getInput, bg="pink")
button.grid(column=1, row=5)

# image = Image.open("app_image.jpeg")
# image.thumbnail((300, 300), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)
# label_image = tk.Label(image=photo)
# label_image.grid(column=1, row=0)

window.mainloop()
