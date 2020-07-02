from functools import reduce

# reduce -> função que reduz uma lista a um elemento

fSoma = lambda x, y: x + y

lista = [1, 2, 3, 4]

soma = reduce(fSoma, lista)
print(soma)