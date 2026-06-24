import numpy as np  # Import NumPy library for numerical operations

# Create a 3x3 identity matrix (diagonal = 1, rest = 0)
I = np.eye(3)

# Define a 3x3 matrix A
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Matrix multiplication of A with identity matrix (A × I = A)
print(f'A X I: \n {np.dot(A, I)}')

# Create a diagonal matrix with given diagonal elements
D = np.diag([1, 7, 9])

# Create a 3x4 matrix filled with zeros
Z = np.zeros((3, 4))

# Print diagonal matrix
print(f'Diagonal Matrix \n {D}')

# Print zero matrix
print(f'Zero Matrix \n {Z}')