# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a matrix of zeros with 2 rows and 3 columns
Z = np.zeros((2, 3))

# Display the zero matrix
print(f'Zero Matrix:\n{Z}')





'''
Explanation
Creating a Zero Matrix
Z = np.zeros((2, 3))
np.zeros() creates an array filled with zeros.
(2, 3) specifies the shape:
2 rows
3 columns
Output
Zero Matrix:
[[0. 0. 0.]
 [0. 0. 0.]]
Matrix Structure
Row	Column 1	Column 2	Column 3
1	0	0	0
2	0	0	0

This is called a 2 × 3 Zero Matrix.

Why Are Zero Matrices Useful?

Zero matrices are commonly used for:

Initializing data structures
Storing results before calculations
Machine Learning algorithms
Scientific computing
Matrix operations
More Examples
3×3 Zero Matrix
np.zeros((3, 3))

Output:

[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
1×5 Zero Matrix
np.zeros((1, 5))

Output:

[[0. 0. 0. 0. 0.]]
Related Functions
np.zeros((2, 3))  # All zeros
np.ones((2, 3))   # All ones
np.eye(3)         # Identity matrix
Key Concept

A Zero Matrix is a matrix in which every element is 0.

[
0
0
	​

0
0
	​

0
0
	​

]

In NumPy, np.zeros(shape) is the quickest way to create one.


'''