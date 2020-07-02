import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3000, 100]

plt.scatter(x, y, label="Meus pontos", color="red", marker="*", s=z)
# plt.scatter(x, y, label="Meus pontos", color="red", marker="^", s=100)
# plt.scatter(x, y, label="Meus pontos", color="red", marker="h", s=100)
# plt.scatter(x, y, label="Meus pontos", color="g", marker="x", s=100)

plt.plot(x, y, color="k", linestyle=":")
# plt.plot(x, y, color="k", linestyle="-.")
# plt.plot(x, y, color="#990000", linestyle="--")

plt.legend()
plt.title('Scatterplot: Gráfico de dispersão')
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show()

# Salvando a figura
plt.savefig("figura1.png", dpi=300)     # pode ser pdf