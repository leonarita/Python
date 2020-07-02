import time

t1 = time.time()
sum = 0

for i in range(1, 1000000):
    sum = sum + i
print(sum)

t2 = time.time()

print(f'Time: {t2-t1}')
