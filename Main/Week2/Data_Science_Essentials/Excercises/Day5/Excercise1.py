# Group Data by a categorical column

# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Import NumPy (not required in this example, but available if needed)
import numpy as np

# Create a dictionary containing student data
data = {
    'Class': ['A', 'B', 'A', 'B', 'C', 'C'],
    'Score': [85, 90, 88, 72, 95, 80],
    'Age': [15, 16, 15, 17, 16, 15]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the original dataset
print(f'Original Dataset:\n{df}')

# Group the data by the 'Class' column
# and calculate the mean of all numeric columns for each class
grouped = df.groupby('Class').mean()

# Display the grouped results
print(grouped)


'''
Explanation
Original Dataset
Class	Score	Age
A	85	15
B	90	16
A	88	15
B	72	17
C	95	16
C	80	15
Grouping Data
grouped = df.groupby('Class').mean()
groupby('Class')
Groups rows based on the values in the Class column.
.mean()
Calculates the average of all numeric columns within each group.
Calculations
Class A

Scores:

85, 88

Average Score:

(85 + 88) / 2 = 86.5

Ages:

15, 15

Average Age:

15.0
Class B

Scores:

90, 72

Average Score:

(90 + 72) / 2 = 81.0

Ages:

16, 17

Average Age:

16.5
Class C

Scores:

95, 80

Average Score:

(95 + 80) / 2 = 87.5

Ages:

16, 15

Average Age:

15.5
Expected Output
       Score   Age
Class
A       86.5  15.0
B       81.0  16.5
C       87.5  15.5
Key Concept

groupby() is one of the most powerful Pandas functions. It allows you to:

Group data by one or more columns
Calculate statistics such as:
mean()
sum()
count()
min()
max()
median()

This process is often called Split → Apply → Combine:

Split the data into groups.
Apply a function (e.g., mean()).
Combine the results into a new DataFrame.


'''
