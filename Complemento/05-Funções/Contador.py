from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.1)
            cont += p
        print('\tFIM')
    else:
        cont=i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.1)
            cont -= p
        print('\tFIM')


contador(1, 10, 1)
print('-' * 40)
print()
contador(10, 0, 2)
print('-' * 40)
print()

ini = int(input('\tInício: '))
fim = int(input('\tFim: '))
pas = int(input('\tPasso: '))
print()
contador(ini, fim, pas)