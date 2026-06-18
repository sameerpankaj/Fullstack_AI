#Select Specific Columns and Filter Rows

# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Load the Iris dataset from a CSV file hosted online
df = pd.read_csv(
    'http://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
)

# Select the 'species' and 'sepal_length' columns from the DataFrame
# Double square brackets are used when selecting multiple columns
selected_columns = df[['species', 'sepal_length']]

# Print the selected columns
print(f'Selected Columns:\n{selected_columns}')

# Filter rows where:
# 1. sepal_length is greater than 5.0
# 2. species is equal to 'setosa'
# The '&' operator combines both conditions
filtered_rows = df[
    (df['sepal_length'] > 5.0) &
    (df['species'] == 'setosa')
]

# Print the filtered rows
print(f'\nFiltered Rows:\n{filtered_rows}')

'''
Explanation
Selecting Multiple Columns
selected_columns = df[['species', 'sepal_length']]
Extracts only the specified columns:
species
sepal_length
Returns a new DataFrame containing those columns.
Filtering Rows
filtered_rows = df[
    (df['sepal_length'] > 5.0) &
    (df['species'] == 'setosa')
]

This applies two conditions:

df['sepal_length'] > 5.0
Selects rows where the sepal length is greater than 5.0.
df['species'] == 'setosa'
Selects rows belonging to the species "setosa".
&
Combines both conditions using a logical AND.
A row must satisfy both conditions to be included.
Example of Matching Rows
sepal_length	species
5.1	setosa
5.4	setosa
5.8	setosa

These rows would appear in filtered_rows because they meet both criteria.

'''