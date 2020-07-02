import numpy as np

array = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]))
p1 = array.reshape(3, 4)
p2 = array.flatten()

print()
print(array)
print()
print(p1)
print()
print(p2)