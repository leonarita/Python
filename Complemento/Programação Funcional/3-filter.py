# filter -> filtra uma lista por uma condição

pares = lambda x: x % 2 == 0

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = filter(pares, lista)
print(list(lista_pares))
