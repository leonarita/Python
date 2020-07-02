import matplotlib.pyplot as plt

percent = [78, 22, 3]
colour = ['blue', 'green', 'red']
label = ["Nitrogen", "Oxigen", "CO2"]

plt.pie(percent, labels=label, colors=colour)
plt.show()