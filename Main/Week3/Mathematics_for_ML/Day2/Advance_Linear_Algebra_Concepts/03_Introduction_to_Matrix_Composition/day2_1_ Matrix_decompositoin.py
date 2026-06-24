import numpy as np  # Import the NumPy library

# Create a 2×2 matrix A
A = np.array([
    [2, 3],
    [1, 4]
])

# Perform Singular Value Decomposition (SVD)
# A = U @ Σ @ Vᵀ
#
# U  : Left singular vectors
# S  : Singular values (returned as a 1D array)
# Vt : Transpose of the right singular vectors (Vᵀ)
U, S, Vt = np.linalg.svd(A)

# Display the left singular vectors
print(f'U: \n {U}')

# Display the singular values
print(f'S: \n {S}')

# Display the transpose of the right singular vectors
print(f'V Transpose: \n {Vt}')