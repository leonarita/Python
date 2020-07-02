import pandas as pd
import random

s = pd.Series([1, 2, 3])
print(s)

print('\n\n')
dates = pd.date_range('2020-05-30', periods=6)
for d in dates:
    print(d)

print('\n\n')
dates = pd.date_range('2020-05-30', periods=1)
data_frame = pd.DataFrame(random.random(), index=dates, columns=['Earning'])
print(data_frame)