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




'''
Explanation
Matrix A
[[1 2]
 [3 4]]
Matrix B
[[5 6]
 [7 8]]
Matrix Addition
A + B

NumPy adds corresponding elements:

[1+5   2+6]
[3+7   4+8]

Result:

[[ 6  8]
 [10 12]]
Output
Addition:
 [[ 6  8]
  [10 12]]
Matrix Subtraction
A - B

NumPy subtracts corresponding elements:

[1-5   2-6]
[3-7   4-8]

Result:

[[-4 -4]
 [-4 -4]]
Output
Subtraction:
 [[-4 -4]
  [-4 -4]]
Element-wise Operations

NumPy performs these operations element by element:

Operation	Formula
Addition	A[i,j] + B[i,j]
Subtraction	A[i,j] - B[i,j]

For matrices to be added or subtracted, they must have the same shape (same number of rows and columns).

Summary
A + B  # Matrix addition
A - B  # Matrix subtraction

These are examples of element-wise matrix operations, which are very common in data science, machine learning, and numerical computing.

'''