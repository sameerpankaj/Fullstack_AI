# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create two 2×2 matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Perform element-wise addition
print('Addition:\n', A + B)

# Perform element-wise subtraction
print('Subtraction:\n', A - B)

# Scalar multiplication
C = 2 * A
print(f'Scalar Multiplication:\n{C}')



'''
Explanation
Matrix A
[[1 2]
 [3 4]]
Scalar Multiplication
C = 2 * A

A scalar is a single number. Here, the scalar is 2.

NumPy multiplies every element of matrix A by 2:

[[1×2  2×2]
 [3×2  4×2]]

Result:

[[2 4]
 [6 8]]
Output
Scalar Multiplication:
[[2 4]
 [6 8]]
Complete Output
Addition:
 [[ 6  8]
  [10 12]]

Subtraction:
 [[-4 -4]
  [-4 -4]]

Scalar Multiplication:
 [[2 4]
  [6 8]]
Key Concept

Matrix operations you've used so far:

Operation	Code
Addition	A + B
Subtraction	A - B
Scalar Multiplication	2 * A

Scalar multiplication is commonly used in:

Linear Algebra
Machine Learning
Computer Graphics
Data Transformations

It scales every value in the matrix by the same factor.


'''