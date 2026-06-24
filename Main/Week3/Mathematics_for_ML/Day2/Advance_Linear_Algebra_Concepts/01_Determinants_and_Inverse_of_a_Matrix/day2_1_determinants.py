import numpy as np  # Import the NumPy library

# Create a 2x2 matrix
A = np.array([
    [2, 3],
    [1, 4]
])

# Calculate the determinant of matrix A
# For a 2x2 matrix [[a, b], [c, d]],
# determinant = (a * d) - (b * c)
determinant = np.linalg.det(A)

# Display the determinant
print(f'Determinant: \n {determinant}')



'''
Explanation

For the matrix:

A=[
2
1
	​

3
4
	​

]

The determinant is:

(2×4)−(3×1)=8−3=5

So the output will be approximately:

Determinant:
5.000000000000001

The small extra decimal places appear because computers store floating-point numbers with limited precision.

'''