#create arrays using built in functions

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a one-dimensional NumPy array with four elements
arr = np.array([1, 2, 3, 4])

# Print the array
print(arr)

# Create a 3x3 array filled with zeros
zeroes = np.zeros((3, 3))

# Print the zeros array
print(zeroes)

# Create a 2x4 array filled with ones
ones = np.ones((2, 4))

# Print the ones array
print(ones)

# Create an array starting from 1 up to (but not including) 10,
# with a step size of 2
range_arr = np.arange(1, 10, 2)

# Print the range array
print(range_arr)

# Create an array of 5 evenly spaced values between 0 and 1 (inclusive)
linspace_array = np.linspace(0, 1, 5)

# Print the evenly spaced array
print(linspace_array)


'''

Output
[1 2 3 4]

[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]

[1 3 5 7 9]

[0.   0.25 0.5  0.75 1.  ]


'''
