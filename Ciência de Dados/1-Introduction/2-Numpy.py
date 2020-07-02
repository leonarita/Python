import numpy as np
from PIL import Image

arr = np.array([1, 2, 3])
print(arr)

print('\n\n')
arr = np.array([(1, 2, 3), (4, 5, 6)])
print(arr)

print('\n\n')
arr = np.array([(1, 2, 3), (4, 5, 6)])
arr = arr.reshape(3, 2)
print(arr)

img = np.array(Image.open(r'C:\\'))
print(img.shape)