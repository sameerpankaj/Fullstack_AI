import numpy as np

A = np.array([[3, 1, 1], [-1, 3, 1], [1, 1, 3]])
U, S, Vt = np.linalg.svd(A)

print(f'U: \n {U}')
print(f'Singular Values: \n {S}')
print(f'V Transpose : \n {Vt}')


#Reconstruct 
Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt

print(f'Reconstructed Matrix \n {reconstructed}')