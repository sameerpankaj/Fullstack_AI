'Change shape of array'


# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a one-dimensional NumPy array with six elements
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the 1D array into a 2D array with 2 rows and 3 columns
reshaped = arr.reshape((2, 3))

# Print the reshaped array
print(reshaped)


'''Output
[[1 2 3]
 [4 5 6]]
'''