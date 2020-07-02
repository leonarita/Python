import numpy as np

a = np.array(([1, 2, 3], [4, 5, 6]))

print()
print(f'First Row: {a[0]}')
print(f'Second Row: {a[1]}')

print()
print(f'First Row, First Element: {a[0][0]}')
print(f'Second Row, First Element: {a[1][0]}')

print()
print(f'First Column: {a[:, 0]}')
print(f'Second Column: {a[:, 1]}')
print(f'Third Column: {a[:, 2]}')

print()
print(f'First Column, First Element: {a[:1, 0]}')
print(f'Second Column, First Element: {a[:1, 1]}')
print(f'Third Column, First Element: {a[:1, 2]}')