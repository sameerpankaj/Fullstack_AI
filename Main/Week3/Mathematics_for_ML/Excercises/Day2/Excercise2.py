import numpy as np  # Import the NumPy library

# Create a 2×2 matrix A
A = np.array([
    [4, -2],
    [1,  1]
])

# Compute the eigenvalues and eigenvectors of A
# eigvals contains the eigenvalues (λ)
# eigvec contains the corresponding eigenvectors as columns
eigvals, eigvec = np.linalg.eig(A)

# Display the eigenvalues
print(f'Eigenvalues: \n {eigvals}')

# Display the eigenvectors
print(f'EigenVectors: \n {eigvec}')