# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Create a Pandas Series with custom index labels
# Values: 10, 20, 30
# Index labels: 'a', 'b', 'c'
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# Print the Series
print(s)


'''
Expected Output
a    10
b    20
c    30
dtype: int64
Explanation
pd.Series() creates a one-dimensional labeled array.

The values are:

[10, 20, 30]

The custom index labels are:

['a', 'b', 'c']

Each value is associated with its corresponding label:

a → 10
b → 20
c → 30
Accessing Values
print(s['a'])  # Output: 10
print(s['b'])  # Output: 20
print(s['c'])  # Output: 30

'''