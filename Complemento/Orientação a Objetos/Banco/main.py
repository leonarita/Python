from conta import Conta, PessoaFisica, PessoaJuridica

op = 0
key = False
print("\n\t\tBem-vindo ao banco!!")

while op != 1 or op != 2:
    op = int(input("\n\n\tConsidere as opções abaixo: \n\t\t1-Cadastrar \n\t\t2-Acessar o sistema \nInforme a opção desejada: "))

    if op == 1:
        tipo = int(input("\n\n Considere as informações abaixo: \n\t 1-Pessoa Física \n\t 2-Pessoa Jurídica \n\t\tInforme qual opção você se encontra: "))

        if (tipo == 1):
            print("\n Insira seus dados abaixo")
            nome = input("\t Informe seu nome: ")
            saldo = float(input("\t Informe seu saldo: "))
            dataNasc = input("\t Informe sua data de nascimento: ")
            rg = input("\t Informe seu RG: ")
            cpf = input("\t Informe seu CPF: ")
            senha = input("\t Informe a senha: ")
            info = PessoaFisica(nome, saldo, dataNasc, rg, cpf, senha)

            file = open("LoginFis", "wb+")
            file.write(cpf)
            file.write(senha)
            file.close()

            file = open("pFis", "wb+")
            file.write(info)
            file.close()
            key = True

        elif (tipo == 2):
            print("\n Insira seus dados abaixo")
            nome = input("\t Informe seu nome: ")
            saldo = float(input("\t Informe seu saldo: "))
            nomeFant = input("\t Informe seu nome fantasia: ")
            cnpj = input("\t Informe seu CNPJ: ")
            rsoc = input("\t Informe a razão social: ")
            senha = input("\t Informe a senha: ")
            info = PessoaFisica(nome, saldo, nomeFant, cnpj, rsoc, senha)

            file = open("LoginJur", "wb+")
            file.write(cnpj)
            file.write(senha)
            file.close()

            file = open("pJur", "wb+")
            file.write(nome)
            file.write(saldo)
            file.write(cnpj)
            file.write(nomeFant)
            file.write(rsoc)
            file.close()
            key = True

        else:
            print("\n\n\nComando inválido!")

    elif op == 2:
        tipo = int(input("\n\n Considere as informações abaixo: \n\t 1-Pessoa Física \n\t 2-Pessoa Jurídica \n\t\tInforme qual opção você se encontra: "))
        linha = 1

        if tipo == 1:
            cpf = input("\t Informe seu CPF: ")
            senha = input("\t Informe a senha: ")

            file = open("LoginFis", "rb+")
            try:
                while True:
                    if file.readline() == cpf and file.readline() == senha:
                        key = True
                        break
            except:
                print("\n\nOcorreu algum erro no sistema")
            finally:
                file.close()

        if tipo == 2:
            cnpj = input("\t Informe seu CNPJ: ")
            senha = input("\t Informe a senha: ")

            file = open("LoginJur", "rb+")
            try:
                while True:
                    if file.readline() == cnpj and file.readline() == senha:
                        key = True
                        break
            except:
                print("\n\nOcorreu algum erro no sistema")
            finally:
                file.close()

if (key == True):
    opcao = 0
    while opcao != 4:
        print("\n\n Considere as opções abaixo: \n\t 1- Consultar saldo \n\t 2- Depositar \n\t 3- Retirar \n\t 4- Sair")
        opcao = int(input("Qual ação você deseja fazer? "))

        if (opcao == 1):
            info.consulta()

        elif (opcao == 2):
            valor = float(input("Quanto deseja depositar? "))
            info.deposito(valor)

        elif (opcao == 3):
            valor = float(input("Quanto deseja retirar? "))
            info.retirada(valor)

        elif opcao == 4:
            print("\n\t\t Obrigado pela preferência! \n\t\t\tVolte sempre")

        else:
            print("\n\t\t Código inválido!")
