import pandas as pd

print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))
print("\n\n")

print(pd.DataFrame({'Bob': ['I liked it', 'It was awful'],
                    'Sue': ['Pretty good', 'Bland']},
                   index=['Product A', 'Product B']))