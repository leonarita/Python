from tkinter import *


class Acesso:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.quadro1 = Frame(master)
        self.quadro1["pady"] = 10
        self.quadro1.pack()

        self.quadro2 = Frame(master)
        self.quadro2["padx"] = 20
        self.quadro2["pady"] = 10
        self.quadro2.pack()

        self.quadro3 = Frame(master)
        self.quadro3["padx"] = 20
        self.quadro3["pady"] = 5
        self.quadro3.pack()

        self.textInicial = Label(self.quadro1, text="Pessoa:")
        self.textInicial["font"] = ("Calibri", "9", "bold")
        self.textInicial.pack()

        self.textInicial = Label(self.quadro2, text="CPF")
        self.textInicial["font"] = ("Calibri", "9", "bold")
        self.textInicial.pack()

        self.textInicial = Label(self.quadro3, text="Senha")
        self.textInicial["font"] = ("Calibri", "9", "bold")
        self.textInicial.pack()


class Application:
    def __init__(self, master=None):
        op = IntVar()
        op.set(0)

        self.fonte = ("Verdana", "8")

        self.quadro1 = Frame(master)
        self.quadro1["pady"] = 10
        self.quadro1.pack()

        self.quadro2 = Frame(master)
        self.quadro2["padx"] = 20
        self.quadro2["pady"] = 10
        self.quadro2.pack()

        self.quadro3 = Frame(master)
        self.quadro3["padx"] = 20
        self.quadro3["pady"] = 5
        self.quadro3.pack()

        self.textInicial = Label(self.quadro1, text="Seja bem-vindo!")
        self.textInicial["font"] = ("Calibri", "9", "bold")
        self.textInicial.pack()

        self.op1 = Radiobutton(self.quadro2, text="Cadastrar", font=self.fonte, variable=op, value=1, width=12)
        self.op1.pack(side=LEFT)
        self.op2 = Radiobutton(self.quadro2, text="Acessar", font=self.fonte, variable=op, value=2, width=12)
        self.op2.pack(side=RIGHT)

        self.btnEntrada = Button(self.quadro3, text="Prosseguir", font=self.fonte, width=12)
        if op == 1:
            self.btnEntrada["command"] = self.Cadastrar
        elif op == 2:
            self.btnEntrada["command"] = self.Acessar
        self.btnEntrada.pack()

    def Acessar(self):
        self.master.destroy()
        Acesso(self.master)

    def Cadastrar(self):
        Acesso(self.master)


app = Tk()
Application(app)
app.mainloop()
