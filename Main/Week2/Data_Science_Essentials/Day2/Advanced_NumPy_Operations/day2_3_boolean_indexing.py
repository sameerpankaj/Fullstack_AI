'''
Boolean Indexing and Filtering
--What is Boolean Indexing?

'''

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a NumPy array with values from 1 to 6
arr = np.array([1, 2, 3, 4, 5, 6])

# Use boolean indexing to select only even numbers
# arr % 2 == 0 creates a boolean mask: [False, True, False, True, False, True]
evens = arr[arr % 2 == 0]

# Print the array containing only even numbers
print('Evens: ', evens)

# Alternative way to print the same result using an f-string
print(f'Evens: {evens}')

# Use boolean indexing to modify the array
# All elements greater than 3 are replaced with 0
arr[arr > 3] = 0

# Print the modified array
print(f'Modified Array: {arr}')

'''
Expected Output
Evens:  [2 4 6]
Evens: [2 4 6]
Modified Array: [1 2 3 0 0 0]
Explanation
arr % 2 == 0
Checks whether each element is even.

Produces a boolean mask:

[False, True, False, True, False, True]
arr[arr % 2 == 0]
Returns only the elements where the condition is True.

Result:

[2 4 6]
arr[arr > 3] = 0
Finds all elements greater than 3.
Replaces them with 0.

Original array:

[1 2 3 4 5 6]

Modified array:

[1 2 3 0 0 0]

This technique is called Boolean Indexing (or Boolean Masking) and is one of the most powerful features of NumPy for filtering and modifying data efficiently.

'''