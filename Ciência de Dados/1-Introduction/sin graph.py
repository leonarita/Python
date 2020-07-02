from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import math

style.use('dark_background')

x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x, y)

plt.xlabel("angle")
plt.ylabel("sine")
plt.title('Sine wave')
plt.show()