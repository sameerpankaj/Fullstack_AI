#DataFrame

# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Create a dictionary containing employee data
# Each key becomes a column name in the DataFrame
data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

'''
Expected Output
    Name  Age
0  Alice   25
1    Bob   30
Explanation
data is a dictionary where:
'Name' contains a list of names.
'Age' contains a list of ages.
pd.DataFrame(data)
Converts the dictionary into a DataFrame.
Dictionary keys become column names.
List elements become row values.
Pandas automatically creates row indexes:
0
1
DataFrame Structure
Index	Name	Age
0	Alice	25
1	Bob	30

A DataFrame is the most commonly used Pandas data structure and is similar to an Excel spreadsheet or a SQL table.
'''