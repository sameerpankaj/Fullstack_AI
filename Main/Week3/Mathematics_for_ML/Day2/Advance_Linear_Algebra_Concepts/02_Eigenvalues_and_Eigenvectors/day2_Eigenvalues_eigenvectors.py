import numpy as np  # Import the NumPy library

# Create matrix A
A = np.array([
    [2, 3],
    [1, 4]
])

# Compute the eigenvalues and eigenvectors of A
# eigenValues contains the eigenvalues (λ)
# eigenvectors contains the corresponding eigenvectors as columns
eigenValues, eigenvectors = np.linalg.eig(A)

# Display the eigenvalues of A
print(f'EigenVal \n {eigenValues}')

# Display the eigenvectors of A
print(f'EigenVector \n {eigenvectors}')

# Create another matrix B
B = np.array([
    [4, 2],
    [1, 1]
])

# Compute the eigenvalues and eigenvectors of B
eigval, eigvec = np.linalg.eig(B)

# Display the eigenvalues of B
print(f'EigenVal \n {eigval}')

# Display the eigenvectors of B
print(f'EigenVector \n {eigvec}')