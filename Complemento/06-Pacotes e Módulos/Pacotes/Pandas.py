import pandas as pd

data = { 'Name': ['Taylor', 'Piyush', 'Renil', 'Jonny'],
         'Age': [27, 17, 18, 32],
         'Address': ['US', 'Surat', 'Ahmedabad', 'Mumbai'],
         'Qualifications': ['Msc', 'MA', 'MCA', 'Phd'] }

d = pd.DataFrame(data)
print(d)