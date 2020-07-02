from matplotlib import pyplot as plt, style

plt.plot([1, 2, 3], [0, 3, 8])
plt.show()

plt.bar([1, 2, 3], [1, 3, 8])
plt.show()

plt.plot([1, 2, 3], [10, 803, 3500])
plt.title('Active Covid Cases')
plt.ylabel('cases')
plt.xlabel('month')
plt.show()

style.use('ggplot')
plt.scatter([1, 2, 3], [1, 3, 8])
plt.show()

