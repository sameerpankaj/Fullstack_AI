#element wise operations

# import numpy as np

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print('Original Matrix: \n', matrix)

# transpose = matrix.T
# print('Transpose:\n', transpose)

# another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# print('Addition: \n', matrix + another_matrix)
# print('Multiplication: \n', matrix * another_matrix)


# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a 3x3 matrix (2D NumPy array)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Print the original matrix
print('Original Matrix: \n', matrix)

# Compute the transpose of the matrix (rows become columns)
transpose = matrix.T

# Print the transposed matrix
print('Transpose:\n', transpose)

# Create another 3x3 matrix
another_matrix = np.array([[9, 8, 7],
                           [6, 5, 4],
                           [3, 2, 1]])

# Print element-wise addition of both matrices
# Each element is added with the corresponding element in the same position
print('Addition: \n', matrix + another_matrix)

# Print element-wise multiplication of both matrices
# This is NOT matrix multiplication, but element-by-element multiplication
print('Multiplication: \n', matrix * another_matrix)