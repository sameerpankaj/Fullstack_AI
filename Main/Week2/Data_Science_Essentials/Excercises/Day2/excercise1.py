#Broadcasting oeprations

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a 3x3 matrix (2D NumPy array)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Create a vector with 3 elements
vector = np.array([1, 0, -1])

# Add the vector to each row of the matrix using broadcasting
# NumPy automatically applies the vector to every row
result_add = matrix + vector

# Print the result of the addition
print(f'Add:\n{result_add}')

# Multiply every element in the matrix by 2
# This is an example of scalar broadcasting
result_mul = matrix * 2

# Print the result of the multiplication
print(f'Multiplication:\n{result_mul}')


'''
Expected Output
Add:
[[2 2 2]
 [5 5 5]
 [8 8 8]]

Multiplication:
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
Explanation
matrix + vector
Uses broadcasting.
The vector [1, 0, -1] is added to each row of the matrix:
[1, 2, 3] + [1, 0, -1] = [2, 2, 2]
[4, 5, 6] + [1, 0, -1] = [5, 5, 5]
[7, 8, 9] + [1, 0, -1] = [8, 8, 8]
matrix * 2
Uses scalar broadcasting.
The scalar 2 is multiplied by every element in the matrix.

Result:

[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]

'''