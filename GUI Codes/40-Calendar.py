from tkinter import *
import calendar


def showCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("CALENDAR")
    new_gui.geometry("550x600")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)

    new_gui.mainloop()


if __name__ == "__main__":
    gui = Tk()
    gui.config(background="white")
    gui.title("CALENDAR")
    gui.geometry("250x140")

    cal = Label(gui, text="Calendar", bg="dark gray", font=("times", 28, 'bold'))
    cal.grid(row=1, column=1)

    year = Label(gui, text="Enter Year", bg="light green")
    year.grid(row=2, column=1)

    year_field = Entry(gui)
    year_field.grid(row=3, column=1)

    Show = Button(gui, text="Show Calendar", fg="Black", bg="red", command=showCal)
    Show.grid(row=4, column=1)

    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
    Exit.grid(row=6, column=1)

    gui.mainloop()
