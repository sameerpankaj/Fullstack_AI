# Mege Two Datasets and Perform Data Transformations

# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Import NumPy (not used in this example, but imported if needed later)
import numpy as np

# Create the first DataFrame containing student information
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Create the second DataFrame containing student scores
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Score': [85, 90, 88]
})

# Display the first dataset
print(f'Dataset1:\n{df1}')

# Display the second dataset
print(f'Dataset2:\n{df2}')

# Merge the two datasets using the 'ID' column
# how='inner' keeps only matching rows from both DataFrames
merged = pd.merge(df1, df2, how='inner', on='ID')

# Display the merged dataset
print(f'Merged Dataset:\n{merged}')

# Create a new column called 'Score_Percentage'
# Since scores are already out of 100, this calculation returns the same values
merged['Score_Percentage'] = (merged['Score'] / 100) * 100

# Display the transformed dataset
print(f'Transformed Dataset:\n{merged}')

'''
Explanation
Creating DataFrames

df1 contains:

ID	Name	Age
1	Alice	25
2	Bob	30
3	Charlie	35

df2 contains:

ID	Score
1	85
2	90
3	88
Merging DataFrames
merged = pd.merge(df1, df2, how='inner', on='ID')
pd.merge() combines two DataFrames.
on='ID' means match rows using the ID column.
how='inner' keeps only rows with matching IDs in both DataFrames.

Result:

ID	Name	Age	Score
1	Alice	25	85
2	Bob	30	90
3	Charlie	35	88
Adding a New Column
merged['Score_Percentage'] = (merged['Score'] / 100) * 100
Creates a new column named Score_Percentage.
Since the scores are already out of 100, the values remain unchanged.

Result:

ID	Name	Age	Score	Score_Percentage
1	Alice	25	85	85.0
2	Bob	30	90	90.0
3	Charlie	35	88	88.0
Note

The calculation:

(merged['Score'] / 100) * 100

simplifies to:

merged['Score']

So the new column contains the same values as the Score column. In a real-world scenario, you might calculate percentages from marks obtained out of a different total, for example:

merged['Percentage'] = (merged['Score'] / 120) * 100

'''