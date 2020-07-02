import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)

y1 = x/2
y2 = x**2
y3 = x**3
y4 = np.sin(x)

fig, janela = plt.subplots(2, 2)

janela[0, 0].plot(x, y1, '.')
janela[0, 1].plot(x, y2, '.r')
janela[1, 0].plot(x, y3, '.y')
janela[1, 1].plot(x, y4, '.g')

fig.legend(['Reta', 'Parábola', 'Cúbida', 'Sin'])
plt.show()