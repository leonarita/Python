# zip -> une duas ou mais listas pelo índice

lista1 = [1, 2, 3, 4]
lista2 = ["abacate", "bola", "cachorro", "elefante"]
lista3 = ["R$2,00", "R$5,00", "não tem preço", "não possui preço"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)