frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

"""
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
"""

inverso = junto[::-1]

print ('Você digitou a frase ', format(junto))
print(junto, inverso)

if inverso==junto:
    print('\n\t\tTemos um palíndromo!')
else:
    print('\n\t\tA frase digitada não é um palíndromo!')