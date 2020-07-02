while True:
    nome = str(input("Insira o nome a ser cadastrado: "))
    senha = str(input("Insira a senha do usuário: "))

    with open("reg.txt", "a") as file:
        file.write(nome)
        file.write('\n')
        file.write(senha)
        file.write('\n')

    op = str(input("\n\tDeseja continuar? [S/N] ")).upper()
    if op=='N':
        break