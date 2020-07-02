# Boxplot (diagrama de caixa)
# -> é uma técnica de visualização de dados em que representa a variação de dados por meio de quartis.

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
    num = random.randint(0, 50)
    vetor.append(num)

plt.boxplot(vetor)
plt.title('Boxplot')
plt.show()

