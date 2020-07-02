from tkinter import *


def fun():

    def autologin():
        username.set("admin")
        password.set("**********")

    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")

    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()

    username = StringVar()
    password = StringVar()

    username_login_entry = Entry(login_screen, textvariable=username)
    username_login_entry.pack()

    l1 = Label(login_screen, text="").pack()
    l2 = Label(login_screen, text="Password").pack()

    username_password_entry = Entry(login_screen, textvariable=password)
    username_password_entry.pack()

    Button(login_screen, text="Auto fill username and password", command=autologin).pack()
    Button(login_screen, text="Login now", width=10, height=1).pack(pady=10)
    login_screen.mainloop()


fun()
