import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print()
print("Horizontal Array: ", np.hstack((array1, array2)))
print()
print("Vertical Array: ", np.vstack((array1, array2)))