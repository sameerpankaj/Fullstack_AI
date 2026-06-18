'''
Pandas in Python
--What is Pandas?
--Pandas Data Structures
    --Series
    --DataFrame
    --


'''


'''
Pandas in Python

Pandas is a powerful Python library used for data analysis and data manipulation. It provides easy-to-use data structures for working with tabular data, similar to spreadsheets or SQL tables.

Pandas is built on top of NumPy and is one of the most important libraries in data science.

Why Use Pandas?
Read and write data from files (CSV, Excel, JSON, etc.)
Clean and preprocess data
Filter and sort data
Handle missing values
Perform statistical analysis
Group and aggregate data
Work with large datasets efficiently
Installing Pandas
pip install pandas
Importing Pandas
import pandas as pd

The alias pd is the standard convention.

Main Data Structures
1. Series

A Series is a one-dimensional labeled array.

import pandas as pd

data = pd.Series([10, 20, 30, 40])

print(data)

Output:

0    10
1    20
2    30
3    40
dtype: int64
2. DataFrame

A DataFrame is a two-dimensional table consisting of rows and columns.

import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22]
}

df = pd.DataFrame(data)

print(df)

Output:

    Name  Age
0   John   25
1  Alice   30
2    Bob   22
Viewing Data
print(df.head())    # First 5 rows
print(df.tail())    # Last 5 rows
print(df.shape)     # Rows and columns
print(df.columns)   # Column names
print(df.info())    # Dataset information
Selecting Data
Select a Column
print(df['Name'])

Output:

0     John
1    Alice
2      Bob
Name: Name, dtype: object
Select Multiple Columns
print(df[['Name', 'Age']])
Filtering Data
print(df[df['Age'] > 25])

Output:

    Name  Age
1  Alice   30
Adding a New Column
df['Salary'] = [50000, 60000, 45000]

print(df)
Basic Statistics
print(df['Age'].mean())
print(df['Age'].max())
print(df['Age'].min())
print(df['Age'].sum())
Reading a CSV File
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())
Writing to a CSV File
df.to_csv('output.csv', index=False)
Handling Missing Values
df.isnull()        # Check missing values
df.dropna()        # Remove missing values
df.fillna(0)       # Replace missing values with 0
Why Pandas is Important

Pandas is used extensively in:

Data Analysis
Data Science
Machine Learning
Business Intelligence
Financial Analysis
Data Engineering
Relationship with NumPy
NumPy  → Fast numerical operations on arrays
Pandas → Data analysis using tables (DataFrames)

Think of NumPy as the foundation for numerical computing, while Pandas provides spreadsheet-like tools for organizing, cleaning, and analyzing real-world data.

'''