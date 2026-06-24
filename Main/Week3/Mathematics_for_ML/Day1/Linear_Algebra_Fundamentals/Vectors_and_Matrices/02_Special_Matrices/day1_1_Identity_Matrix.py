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

# Create a 3×3 Identity Matrix
I = np.eye(3)

# Display the Identity Matrix
print(f'Identity Matrix:\n{I}')




'''
Explanation
Creating an Identity Matrix
I = np.eye(3)
np.eye(n) creates an n × n Identity Matrix.
Here, 3 means a 3 × 3 matrix.
Output
Identity Matrix:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
What is an Identity Matrix?

An Identity Matrix is a square matrix where:

All diagonal elements are 1
All other elements are 0

For a 3×3 identity matrix:

I=
	​

1
0
0
	​

0
1
0
	​

0
0
1
	​

	​

Why is it Important?

The identity matrix acts like the number 1 in normal multiplication.

For any compatible matrix A:

A×I=A

and

I×A=A
Example
A = np.array([
    [1, 2],
    [3, 4]
])

I = np.eye(2)

print(A @ I)

Output:

[[1 2]
 [3 4]]

The matrix remains unchanged.

Common Identity Matrices
2×2
[[1. 0.]
 [0. 1.]]
3×3
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
4×4
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
Key Concept
np.eye(n)

creates an n × n Identity Matrix, which is widely used in:

Linear Algebra
Matrix Operations
Machine Learning
Computer Graphics
Solving Systems of Equations

It plays the same role for matrices that 1 plays for ordinary numbers.
	
'''