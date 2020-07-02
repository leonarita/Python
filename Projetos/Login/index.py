# importar as bibliotecas
from tkinter import *
from tkinter import messagebox, ttk

from Projetos.Login import database

# Criar a janela
jan = Tk()

# Carregar imagens
logo = PhotoImage(file="icons/logo.png")


def Register():

    # Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    # Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=100, y=66)

    def RegisterToDatabase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if Name == "" or Email == "" or User == "" or Pass == "":
            messagebox.showerror(title="Register Error", message="Preencha todos os campos!")
        else:
            database.cursor.execute(f"INSERT INTO Users (Name, Email, User, Password) VALUES ('{Name}', '{Email}', '{User}', '{Pass}')")
            database.conn.commit()  # Salva as alterações
            messagebox.showinfo(title="Register Info", message="Account created sucessfully")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDatabase)
    Register.place(x=100, y=225)

    def BackToLogin():

        # Removendo widgets de cadastrp
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        # Trazendo os botões de login de volta
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)


def login():
    database.cursor.execute(f"SELECT User, Password FROM Users WHERE (User='{UserEntry.get()}' and Password='{PassEntry.get()}')")
    VerifyLogin = database.cursor.fetchall()   # Pega todos os dados, enquanto o fetchone pega apenas um

    try:
        if VerifyLogin == [(UserEntry.get(), PassEntry.get())] :
            messagebox.showinfo(title="Login Info", message="Acesso confirmado, bem vindo!")
        else:
            messagebox.showwarning(title="Login Info", message="Acesso negado!!")
    except:
        messagebox.showerror(title="Login Info", message="Acesso negado!!")


# Widgets
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)        # Impede maximizar/minimizar
jan.attributes("-alpha", 0.9)                   # Gera o fundo parcialmente transparente
jan.iconbitmap(default="icons/logoIcon.ico")    # Insere um ícone

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")    # Container à esquerda
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")    # Container à direita
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=150, y=160)

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=login)
LoginButton.place(x=100, y=225)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()
