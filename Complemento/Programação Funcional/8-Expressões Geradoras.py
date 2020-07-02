l = [x ** 2 for x in range(10) if x % 2 == 0]
print(l)
print(iter(l) is l)     # False

print()
g = (x ** 2 for x in range(10) if x % 2 == 0)
print(g)
print(iter(g) is g)     # True

print()
for i in g:
    print(i)

print()
print(list(g))
print(list((x ** 2 for x in range(10) if x % 2 == 0)))