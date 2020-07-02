from tkinter import *
from tkinter import messagebox


def Information():
    top = Tk()
    top.geometry("100x100")
    messagebox.showinfo("Information", "Information")
    top.mainloop()


def Warning():
    top = Tk()
    top.geometry("100x100")
    messagebox.showwarning("Warning", "Warning")
    top.mainloop()


def Error():
    top = Tk()
    top.geometry("100x100")
    messagebox.showerror("Error", "Error")
    top.mainloop()


def Question():
    top = Tk()
    top.geometry("100x100")
    messagebox.askquestion("Confirm", "Are you sure?")
    top.mainloop()


def Cancel():
    top = Tk()
    top.geometry("100x100")
    messagebox.askokcancel("Redirect", "Redirecting...")
    top.mainloop()


def YesNo():
    top = Tk()
    top.geometry("100x100")
    messagebox.askyesno("Application", "Go it?")
    top.mainloop()


def Retry():
    top = Tk()
    top.geometry("100x100")
    messagebox.askretrycancel("Application", "Try again?")
    top.mainloop()


op = 1
while op != 8:
    op = int(input("\n\nInsira 1 (Information), 2 (Warning), 3 (Error), 4 (Question), 5 (Cancel), "
                   "6 (YesNo), 7 (Retry) ou 8 (Sair) : "))

    if op == 1:
        Information()
    elif op == 2:
        Warning()
    elif op == 3:
        Error()
    elif op == 4:
        Question()
    elif op == 5:
        Cancel()
    elif op == 6:
        YesNo()
    elif op == 7:
        Retry()
    elif op == 8:
        break
    else:
        continue
