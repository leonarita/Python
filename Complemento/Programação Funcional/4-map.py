# map -> realiza uma aplicação em todos os elementos de uma lista

dobro = lambda x: x * 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valor_dobrado = list(map(dobro, lista))
print(valor_dobrado)
