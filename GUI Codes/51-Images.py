from tkinter import *

root = Tk()
root.geometry("635x685")

new1 = PhotoImage(file="images(1).png")
myimage1 = Label(image=new1)
myimage1.grid(row=0, column=0)

new2 = PhotoImage(file="images(2).png")
myimage2 = Label(image=new1)
myimage2.grid(row=0, column=1)

new3 = PhotoImage(file="images(3).png")
myimage3 = Label(image=new1)
myimage3.grid(row=1, column=0)

new4 = PhotoImage(file="images(4).png")
myimage4 = Label(image=new1)
myimage4.grid(row=1, column=1)

new5 = PhotoImage(file="images(5).png")
myimage5 = Label(image=new1)
myimage5.grid(row=2, column=0)

new6 = PhotoImage(file="images(6).png")
myimage6 = Label(image=new1)
myimage6.grid(row=2, column=1)

root.mainloop()