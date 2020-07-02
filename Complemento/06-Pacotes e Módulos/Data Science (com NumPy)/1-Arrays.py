import numpy as np

list1 = [1, 2, 3, 4, 5]
array = np.array(list1)

print(array)
print(type(list1))
print(type(array))

print()
array += 50
print(array)

print()
array2 = np.array([1, 2, 3, 4, 5])
print(array2.shape)
print(array2.dtype)