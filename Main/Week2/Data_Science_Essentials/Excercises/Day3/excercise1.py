#Load and Explore a Sample Dataset

#url of dataset
#http://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Load the Iris dataset from a CSV file hosted online
df = pd.read_csv(
    'http://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
)

# Display the first 5 rows of the dataset
# Useful for quickly inspecting the data
print('First 5 rows:\n', df.head())

# Display the last 5 rows of the dataset
# Useful for checking the end of the dataset
print('Last 5 rows:\n', df.tail())

# Display information about the dataset
# Includes:
# - Number of rows and columns
# - Column names
# - Data types
# - Non-null values
print(df.info())

# Display descriptive statistics for numerical columns
# Includes:
# - Count
# - Mean
# - Standard deviation
# - Minimum value
# - 25%, 50%, and 75% percentiles
# - Maximum value
print(df.describe())


'''
Explanation
pd.read_csv()
df = pd.read_csv(...)
Reads data from a CSV file.
Stores the data in a Pandas DataFrame.
df.head()
df.head()
Displays the first 5 rows of the dataset.
Useful for understanding the structure and sample data.
df.tail()
df.tail()
Displays the last 5 rows of the dataset.
df.info()
df.info()

Provides information such as:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):

It shows:

Number of rows
Number of columns
Column names
Data types
Missing values
df.describe()
df.describe()

Generates summary statistics for numeric columns:

Statistic	Meaning
count	Number of values
mean	Average value
std	Standard deviation
min	Minimum value
25%	First quartile
50%	Median
75%	Third quartile
max	Maximum value

This is one of the quickest ways to understand a dataset before performing analysis.

Common Data Exploration Workflow
df.head()      # View first rows
df.tail()      # View last rows
df.info()      # Check structure
df.describe()  # Summary statistics

These four commands are typically the first things data analysts run when working with a new dataset.

'''