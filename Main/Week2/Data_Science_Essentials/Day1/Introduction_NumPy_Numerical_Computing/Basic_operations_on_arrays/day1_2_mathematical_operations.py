#mathematical operatins on arrays

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a NumPy array containing the values 4, 16, and 25
arr = np.array([4, 16, 25])

# Calculate and print the square root of each element in the array
print(np.sqrt(arr))

# Calculate and print the sum of all elements in the array
print(np.sum(arr))

# Calculate and print the mean (average) of the array elements
print(np.mean(arr))

# Find and print the maximum value in the array
print(np.max(arr))


'''

Output
[2. 4. 5.]
45
15.0
25
Explanation
np.sqrt(arr) → Returns the square root of each element: [√4, √16, √25]
np.sum(arr) → Adds all elements: 4 + 16 + 25 = 45
np.mean(arr) → Calculates the average: 45 / 3 = 15.0
np.max(arr) → Finds the largest value in the array: 25


'''