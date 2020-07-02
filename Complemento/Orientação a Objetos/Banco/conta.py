class Conta:

    def __init__(self, nome, saldo, senha):
        self.nome = nome
        self.saldo = saldo
        self.senha = senha

    def consulta(self):
        print("\n\t\t Seu saldo é ", self.saldo)

    def deposito(self, valor):
        self.saldo += valor
        print("\n\t\t Seu saldo é ", self.saldo)

    def retirada(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print("\n\t\t Seu saldo é ", self.saldo)
        else:
            print("\n\t\t Saldo insuficiente! Se desejar, é possível pedir um empréstimo com juros de 12%.")


class PessoaFisica(Conta):
    def __init__(self, nome, saldo, dataNasc, rg, cpf, senha):
        super(PessoaFisica, self).__init__(nome, saldo, senha)
        self.dataNasc = dataNasc
        self.__rg = rg
        self.__cpf = cpf


class PessoaJuridica(Conta):
    def __init__(self, nome, saldo, nomeFant, cnpj, rsoc, senha):
        super(PessoaJuridica, self).__init__(nome, saldo, senha)
        self.nomeFant = nomeFant
        self.__cnpj = cnpj
        self.__razaoSocial = rsoc
