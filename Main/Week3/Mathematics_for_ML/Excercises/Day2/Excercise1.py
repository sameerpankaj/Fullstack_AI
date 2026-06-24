import numpy as np  # Import the NumPy library for matrix operations

# Create a 3×3 matrix A
A = np.array([
    [2, 3, 1],
    [4, 5, 6],
    [7, 8, 9]
])

# Calculate the determinant of matrix A
# The determinant indicates whether the matrix is invertible.
# If determinant = 0, the matrix has no inverse.
determinant = np.linalg.det(A)

# Calculate the inverse of matrix A
# np.linalg.inv() works only if the determinant is non-zero.
inverse = np.linalg.inv(A)

# Display the determinant
print(f'Determinant: \n {determinant}')

# Display the inverse matrix
print(f'Inverse: \n {inverse}')