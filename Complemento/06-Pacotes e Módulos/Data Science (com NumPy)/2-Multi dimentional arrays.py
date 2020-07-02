import numpy as np

twoD_array = np.array(([1, 2, 3], [4, 5, 6]))
threeD_array = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))

print(np.shape(twoD_array))
print(np.shape(threeD_array))

a = np.zeros((3, 3), dtype=int, order="C")
b = np.ones((3, 3), dtype=int, order="C")

print()
print(a)
print()
print(b)