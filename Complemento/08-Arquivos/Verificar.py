def contaLinhasNoArquivo():
    linha = 0
    file = open("reg.txt", "r")
    while file.readline() != '':
        linha += 1
    return linha


quant = contaLinhasNoArquivo()

while True:
    nome = str(input("Nome: "))
    senha = str(input("Senha: "))

    try:
        with open("reg.txt", "r") as file:
            for i in range(0, quant+1, 2):
                no = file.readline()
                se = file.readline()
                if nome+'\n' == no and senha+'\n' == se:
                    print("\n\n\t\tLOGIN BEM SUCEDIDO! ")
                    break
            else:
                print("\n\n\t\tLOGIN MAL SUCEDIDO! ")
    except:
        print("\n\n\t\tERRO!")

    op = str(input("\n\tDeseja continuar? [S/N] ")).upper()
    if op == 'N':
        break
