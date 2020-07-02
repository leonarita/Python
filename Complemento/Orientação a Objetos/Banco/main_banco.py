from conta import Conta, PessoaFisica, PessoaJuridica

tipo = 0
op=0
while tipo>2 or tipo<1:
    print ("BEM VINDO AO BANCO!")

    tipo = int (input("\n\n Considere as informações abaixo: \n\t 1-Pessoa Física \n\t 2-Pessoa Jurídica \n\t\tInforme qual opção você se encontra: "))

    if (tipo==1):
        print ("\n Insira seus dados abaixo")
        nome = input ("\t Informe seu nome: ")
        saldo = float (input("\t Informe seu saldo: "))
        dataNasc = input ("\t Informe sua data de nascimento: ")
        rg = input ("\t Informe seu RG: ")
        cpf = input ("\t Informe seu CPF: ")
        senha = input ("\t Informe a senha: ")
        info = PessoaFisica (nome, saldo, dataNasc, rg, cpf, senha)

    elif (tipo==2):
        print ("\n Insira seus dados abaixo")
        nome = input ("\t Informe seu nome: ")
        saldo = float (input("\t Informe seu saldo: "))
        nomeFant = input ("\t Informe seu nome fantasia: ")
        cnpj = input ("\t Informe seu CNPJ: ")
        rsoc = input("\t Informe a razão social: ")
        senha = input("\t Informe a senha: ")
        info = PessoaFisica (nome, saldo, nomeFant, cnpj, rsoc, senha)

    else:
        print ("\n\n\nComando inválido!")

opcao = 0
while opcao != 4 :
    print ("\n\n Considere as opções abaixo: \n\t 1- Consultar saldo \n\t 2- Depositar \n\t 3- Retirar \n\t 4- Sair")
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
        print ("\n\t\t Obrigado pela preferência! \n\t\t\tVolte sempre")

    else:
        print ("\n\t\t Código inválido!")