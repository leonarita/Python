import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)

print(len(x))
print(max(x))
print(min(x))

print(f"\n {x} \n")

y = 2*x
plt.plot(x, y, '*')
plt.title('Título do Gráfico')
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show()

y2 = x**2
plt.plot(x, y2, 'o')
# plt.plot(x, y2, '.g') -> green
plt.show()

plt.plot(x, y, '.r')    # red
plt.plot(x, y2, '.y')   # yellow
plt.legend(['Reta', 'Parábola'])
plt.title('Título do Gráfico')
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show()

