'Slicing Array'


# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a NumPy array with five elements
arr = np.array([10, 20, 30, 40, 50])

# Slice the array from index 1 to 3 (end index 4 is not included)
print(arr[1:4])

# Slice the array from index 3 to the end of the array
print(arr[3:])

