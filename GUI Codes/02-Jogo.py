# importa o módulo random
import random

# armazena a vida do player
player_vida = 500
# armazena o sp do player
player_sp = 100
# vida padrão de um inimigo
inimigo_vida = 50

# determina o número de inimigos
n = int(input("Digite o número de inimigos: "))

# vetor que armazena todos os inimigos
inimigos = []

# adicionamos ao vetor um vetor com 2 componentes: o número do inimigo e sua vida
for i in range(n):
    inimigos.append([i + 1, inimigo_vida])

# enquanto essa variável for True, estaremos rodando o jogo
jogando = True
while jogando:
    print("Vida: ", player_vida)
    print("SP: ", player_sp)

    atk = int(input("Deseja (1) atacar ou (2) curar? "))

    if atk == 1:
        # escolhendo aleatoriamento um inimigo para ser atacado
        selecionado = random.choice(inimigos)

        # determinar o dano causado
        dano = random.randint(10, 15)

        # imprimir essas informações para o usuário
        print("\tCausou %i de dano ao inimigo %i!" % (dano, selecionado[0]))

        # diminuir a vida do inimigo o dano
        selecionado[1] -= dano

        # se a vida do inimigo for zerada, devemos:
        if selecionado[1] <= 0:
            # dizer que o inimigo morreu
            print("\t\tInimigo %i morreu!" % selecionado[0])
            # e remover esse inimigo da lista de inimigos
            inimigos.remove(selecionado)

    # caso contrário, ele escolhe curar
    else:
        # só podemos curar se o sp do player for maior do que 10
        if player_sp >= 10:
            # escolhemos um valor aleatório para a cura
            cura = random.randint(10, 15)
            # imprimimos quanto o player recebeu de cura
            print("\tVocê recebeu %i de vida!" % cura)
            # adicionamos isso à vida do player
            player_vida += cura
            # e diminuimos em 10 o sp do player

        # se o player tiver menos de 10 de sp
        else:
            # imprimimos que o player não pode se curar
            print("\tsp insuficiente!")

    # depois disso, é a vez de os inimigos atacarem
    for inimigo in inimigos:
        # escolhemos se o inimigo vai acertar ou errar
        # o inimigo tem 75% de chance de acertar
        acertou = bool(random.choice([1, 1, 1, 0]))

        # se ele acertar, devemos:
        if acertou:
            # escolher um dano causado pelo player
            dano = random.randint(1, 3)
            # imprimir a mensagem de dano
            print("\tInimigo %i causou %i de dano!" % (inimigo[0], dano))
            # diminuir a vida do player
            player_vida -= dano

        # caso contrário
        else:
            # devemos informar que o inimigo errou
            print("\tInimigo %i errou o ataque!" % inimigo[0])

    # depois devemos aumentar o sp do player
    if player_sp < 100:
        # aumentamos em 3 toda rodada
        player_sp += 3

    # mas se o player nunca pode ter mais de 100 de sp
    if player_sp > 100:
        player_sp = 100

    # se a vida do player for menor que zero, ele perdeu
    if player_vida <= 0:
        print("\t\t\tPerdeu o jogo!")
        jogando = False

    # se o nímero de inimigos for zero, ele venceu
    if len(inimigos) == 0:
        print("\t\t\tParabéns! Você ganhou o jogo!")
        jogando = False