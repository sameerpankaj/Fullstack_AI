'''
Generate Arrays for Basic Mathematical operations
'''


# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create an array with values from 1 to 5
a = np.arange(1, 6)

# Create an array with values from 6 to 10
b = np.arange(6, 11)

# Perform element-wise addition of arrays a and b
print('Add: ', a + b)

# Perform element-wise subtraction of arrays a and b
print('Sub: ', a - b)

# Perform element-wise multiplication of arrays a and b
print('Mul: ', a * b)

# Perform element-wise division of arrays a and b
print('Div: ', a / b)