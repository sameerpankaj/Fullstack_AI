# Calculate Summary Statistics for Grouped Data

# Import the Pandas library and assign it the alias 'pd'
import pandas as pd

# Create a dictionary containing student data
data = {
    'Class': ['A', 'B', 'A', 'B', 'C', 'C'],
    'Score': [85, 90, 88, 72, 95, 80],
    'Age': [15, 16, 15, 17, 16, 15]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Group the data by the 'Class' column and calculate the mean
grouped = df.groupby('Class').mean()

# Perform multiple aggregations on grouped data
# For the 'Score' column:
#   - Calculate mean, maximum, and minimum values
# For the 'Age' column:
#   - Calculate mean, maximum, and minimum values
stats = df.groupby('Class').agg(
    {
        'Score': ['mean', 'max', 'min'],
        'Age': ['mean', 'max', 'min']
    }
)

# Display the aggregated statistics
print(stats)

'''
Explanation
Grouping Data
df.groupby('Class')

Groups all rows according to the values in the Class column:

Class A
Class B
Class C
Using agg()
.agg({
    'Score': ['mean', 'max', 'min'],
    'Age': ['mean', 'max', 'min']
})

The agg() method allows multiple aggregation functions to be applied to multiple columns at once.

For each class, Pandas calculates:

Score

Mean (average)
Maximum
Minimum

Age

Mean (average)
Maximum
Minimum
Calculations
Class A

Scores:

85, 88
Mean = 86.5
Max = 88
Min = 85

Ages:

15, 15
Mean = 15.0
Max = 15
Min = 15
Class B

Scores:

90, 72
Mean = 81.0
Max = 90
Min = 72

Ages:

16, 17
Mean = 16.5
Max = 17
Min = 16
Class C

Scores:

95, 80
Mean = 87.5
Max = 95
Min = 80

Ages:

16, 15
Mean = 15.5
Max = 16
Min = 15
Expected Output
      Score          Age
       mean max min mean max min
Class
A      86.5  88  85 15.0  15  15
B      81.0  90  72 16.5  17  16
C      87.5  95  80 15.5  16  15
Key Concept

agg() (Aggregation) is useful when you want to calculate multiple statistics simultaneously for grouped data.

Common aggregation functions include:

'mean'   # Average
'sum'    # Total
'count'  # Number of values
'max'    # Largest value
'min'    # Smallest value
'median' # Middle value
'std'    # Standard deviation

'''