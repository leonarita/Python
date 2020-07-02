import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

plt.scatter(x, y, label="Meus pontos", color="r")
plt.plot(x, y)
plt.legend()
plt.title('Scatterplot: Gráfico de dispersão')
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show()