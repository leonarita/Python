galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Desejar continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break
média = soma / len(galera)

print('-' * 30)
print(f'\nA) Ao todo, temos {len(galera)} pessoas cadastradas.')
print(f'\nb) A média de idade é de {média:5.2f} anos.')
print('\nC) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'Ff':
        print(f'{p["nome"]} ', end='')
print('\n\nD) Lista das pessoas que estão em cima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}       ', end='')
        print()
print('\n\n<<ENCERRADO>>')