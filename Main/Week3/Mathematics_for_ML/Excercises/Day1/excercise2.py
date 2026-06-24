import numpy as np

# Create a 3×3 matrix
M = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Create a vector
V = np.array([1, 0, -1])

# Matrix-vector multiplication
result = np.dot(M, V)

print(f'Matrix-Vector Multiplication:\n{result}')




'''
Explanation
Matrix
M=
	​

1
4
7
	​

2
5
8
	​

3
6
9
	​

	​

Vector
V=
	​

1
0
−1
	​

	​

How Matrix-Vector Multiplication Works

Each row of the matrix is multiplied by the vector:

First Row
(1×1)+(2×0)+(3×−1)
1+0−3=−2
Second Row
(4×1)+(5×0)+(6×−1)
4+0−6=−2
Third Row
(7×1)+(8×0)+(9×−1)
7+0−9=−2
Result
	​

−2
−2
−2
	​

	​

Output
Matrix-Vector Multiplication:
[-2 -2 -2]
What np.dot(M, V) Does
result = np.dot(M, V)
M is a 3×3 matrix
V is a 3-element vector
NumPy performs row × vector multiplication
The result is a 1D array with 3 elements
Alternative Syntax
result = M @ V

This gives the same output and is often preferred because it clearly represents matrix multiplication.

Real-World Applications

Matrix-vector multiplication is used extensively in:

Machine Learning
Neural Networks
Computer Graphics
Physics Simulations
Data Transformations

It is one of the most fundamental operations in linear algebra and data science.


'''