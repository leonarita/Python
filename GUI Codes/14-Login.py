from tkinter import *
import tkinter.messagebox as mess

root = Tk()
root.title("Login")
userlist = {"admin": "password", "guest": "passwordl"}


def submit(event):
    user3 = user2.get()

    if user3 in userlist:
        pass4 = pass2.get()
        if pass4 == userlist[user3]:
            pass2.delete(0, END)
            mess.showinfo("Network Msg", "Welcome " + user2.get().title())
    else:
        user2.delete(0, END)
        pass2.delete(0, END)
        mess.showerror("Error", "Incorrect Login")


user1 = Label(root, text="Username")
user1.grid(row=0, column=0)

user2 = Entry(root)
user2.grid(row=0, column=1)

pass1 = Label(root, text="Password")
pass1.grid(row=2, column=0)

pass2 = Entry(root, show="*", bg="red")
pass2.bind("<Return>", submit)
pass2.grid(row=2, column=1)

root.mainloop()