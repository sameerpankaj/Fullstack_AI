import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df = pd.read_csv('data.csv')
df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx', index=False)