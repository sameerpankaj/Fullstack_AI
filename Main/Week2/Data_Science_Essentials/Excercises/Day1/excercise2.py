#Create 3x3 Matrix and perform operations

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a 3x3 matrix (2D NumPy array)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print the original matrix
print('Original Matrix: \n', matrix)

# Compute the transpose of the matrix (rows become columns)
transpose = matrix.T

# Print the transposed matrix
print('Transpose:\n', transpose)