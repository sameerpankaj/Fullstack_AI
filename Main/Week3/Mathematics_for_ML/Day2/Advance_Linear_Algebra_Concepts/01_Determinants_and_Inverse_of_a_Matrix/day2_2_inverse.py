import numpy as np  # Import the NumPy library for matrix operations

# Create a 2×2 matrix A
A = np.array([
    [2, 3],
    [1, 4]
])

# Compute the inverse of matrix A
# np.linalg.inv() returns the inverse of a square matrix
# A matrix must have a non-zero determinant to be invertible
inverse = np.linalg.inv(A)

# Display the inverse matrix
print(f'Inverse of A: \n {inverse}')


'''
Expected Output
Inverse of A:
[[ 0.8 -0.6]
 [-0.2  0.4]]
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
Determinant:
det(A)=(2×4)−(3×1)=5
Inverse formula:
A
−1
=
5
1
	​

[
4
−1
	​

−3
2
	​

]
Simplifying:
A
−1
=[
0.8
−0.2
	​

−0.6
0.4
	​

]

You can verify the result by multiplying A and A
−1
, which gives the identity matrix:

A⋅A
−1
=[
1
0
	​

0
1
	​

]


'''