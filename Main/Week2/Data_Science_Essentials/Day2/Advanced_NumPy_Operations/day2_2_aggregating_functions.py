'''
Aggregation functions
--aggregation fumctions compute summary statistics for arrays
--common functions

'''

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a 2x3 NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Calculate and print the sum of all elements in the array
print('Sum: ', np.sum(arr))

# Calculate and print the mean (average) of all elements
print('Mean: ', np.mean(arr))

# Find and print the maximum value in the array
print('Max: ', np.max(arr))

# Find and print the minimum value in the array
print('Min: ', np.min(arr))

# Calculate and print the standard deviation of all elements
print('Standard Deviation: ', np.std(arr))

# Calculate and print the sum of each row
# axis=1 means perform the operation across columns for each row
print('Sum along rows: ', np.sum(arr, axis=1))

# Calculate and print the sum of each column
# axis=0 means perform the operation across rows for each column
print('Sum along columns: ', np.sum(arr, axis=0))


'''
Expected Output
Sum:  21
Mean:  3.5
Max:  6
Min:  1
Standard Deviation:  1.707825127659933
Sum along rows:  [ 6 15]
Sum along columns:  [5 7 9]
Explanation
np.sum(arr) → Adds all elements: 1 + 2 + 3 + 4 + 5 + 6 = 21
np.mean(arr) → Calculates the average: 21 / 6 = 3.5
np.max(arr) → Returns the largest value: 6
np.min(arr) → Returns the smallest value: 1
np.std(arr) → Calculates the standard deviation, a measure of how spread out the values are.
np.sum(arr, axis=1) → Sums each row:
Row 1: 1 + 2 + 3 = 6
Row 2: 4 + 5 + 6 = 15
np.sum(arr, axis=0) → Sums each column:
Column 1: 1 + 4 = 5
Column 2: 2 + 5 = 7
Column 3: 3 + 6 = 9

'''