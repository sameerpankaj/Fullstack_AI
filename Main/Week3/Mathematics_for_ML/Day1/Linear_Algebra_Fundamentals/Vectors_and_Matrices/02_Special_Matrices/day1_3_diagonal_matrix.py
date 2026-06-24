# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a diagonal matrix
D = np.diag([1, 2, 3])

# Display the diagonal matrix
print(f'Diagonal Matrix:\n{D}')




'''
Explanation
Creating a Diagonal Matrix
D = np.diag([1, 2, 3])
np.diag() creates a matrix with the given values on the main diagonal.
All other elements are set to 0.
Output
Diagonal Matrix:
[[1 0 0]
 [0 2 0]
 [0 0 3]]
Matrix Structure
	Col 1	Col 2	Col 3
Row 1	1	0	0
Row 2	0	2	0
Row 3	0	0	3
What is a Diagonal Matrix?

A Diagonal Matrix is a square matrix where:

Non-diagonal elements are all 0
Diagonal elements can be any values
D=
	​

1
0
0
	​

0
2
0
	​

0
0
3
	​

	​

Examples
2×2 Diagonal Matrix
np.diag([5, 8])

Output:

[[5 0]
 [0 8]]
4×4 Diagonal Matrix
np.diag([1, 2, 3, 4])

Output:

[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
Difference Between Common Matrix Types
Matrix Type	Example
Zero Matrix	[[0,0],[0,0]]
Identity Matrix	[[1,0],[0,1]]
Diagonal Matrix	[[5,0],[0,8]]
Key Concept
np.diag([1, 2, 3])

creates a diagonal matrix whose diagonal entries are 1, 2, and 3.

Diagonal matrices are important in:

Linear Algebra
Eigenvalues and Eigenvectors
Machine Learning
Scientific Computing
Matrix Transformations

An identity matrix is actually a special type of diagonal matrix where all diagonal values are 1.


'''