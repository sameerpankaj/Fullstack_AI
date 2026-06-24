# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create two 2×2 matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [9, 8],
    [7, 6]
])

# Matrix addition
print(f'Addition:\n{A + B}')

# Matrix subtraction
print(f'Subtraction:\n{A - B}')

# Scalar multiplication
print(f'Scalar Multiplication:\n{3 * A}')


'''
Note on Your Code

You wrote:

print(f'Addition: \ {A + B}')
print(f'Subtraction: \ {A - B}')

The \ is unnecessary and will simply be printed as a character. To move the matrix to a new line, use \n:

print(f'Addition:\n{A + B}')
print(f'Subtraction:\n{A - B}')
Output
Addition
[[10 10]
 [10 10]]

Because:

[[1+9  2+8]
 [3+7  4+6]]
Subtraction
[[-8 -6]
 [-4 -2]]

Because:

[[1-9  2-8]
 [3-7  4-6]]
Scalar Multiplication
[[ 3  6]
 [ 9 12]]

Because every element of A is multiplied by 3:

[[1×3  2×3]
 [3×3  4×3]]
Complete Output
Addition:
[[10 10]
 [10 10]]

Subtraction:
[[-8 -6]
 [-4 -2]]

Scalar Multiplication:
[[ 3  6]
 [ 9 12]]

This example demonstrates three fundamental matrix operations in NumPy:

A + B → Matrix Addition
A - B → Matrix Subtraction
3 * A → Scalar Multiplication

'''