# Clean a Dataset by Handling Missing Values and Renaming Columns

# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Import NumPy for handling missing values (NaN)
import numpy as np

# Create a sample dataset with some missing values
data = {
    'Name': ['Alice', 'Bob', np.nan, 'David'],
    'Age': [25, np.nan, 30, 35],
    'Score': [85, 90, np.nan, 88]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the original dataset
print(f'Original Dataset:\n{df}')

# Fill missing values in the 'Age' column with the mean age
# Mean Age = (25 + 30 + 35) / 3 = 30
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing values in the 'Score' column using interpolation
# The missing value is estimated based on neighboring values
df['Score'] = df['Score'].interpolate()

# Display the cleaned dataset
print(f'Dataset after handling missing values:\n{df}')

# Rename columns for better readability
df = df.rename(columns={
    'Name': 'Student_Name',
    'Score': 'Exam_Score'
})

# Display the dataset after renaming columns
print(f'Dataset after renaming columns:\n{df}')

'''
Explanation
Creating the Dataset
np.nan
Represents a missing value in Pandas/NumPy.

Original dataset:

    Name   Age  Score
0  Alice  25.0   85.0
1    Bob   NaN   90.0
2    NaN  30.0    NaN
3  David  35.0   88.0
Filling Missing Age Values
df['Age'].fillna(df['Age'].mean())
Calculates the average age:
(25 + 30 + 35) / 3 = 30
Replaces the missing age with 30.
Interpolating Scores
df['Score'].interpolate()
Estimates missing values using nearby values.
The missing score lies between 90 and 88.
90 → 89 → 88
Missing score becomes 89.
Renaming Columns
df.rename(columns={
    'Name': 'Student_Name',
    'Score': 'Exam_Score'
})

Changes:

Old Name	New Name
Name	Student_Name
Score	Exam_Score
Final Dataset
  Student_Name   Age  Exam_Score
0        Alice  25.0        85.0
1          Bob  30.0        90.0
2          NaN  30.0        89.0
3        David  35.0        88.0

This example demonstrates three common data-cleaning tasks in Pandas:

Handling missing values with fillna()
Estimating missing values with interpolate()
Renaming columns with rename()

'''