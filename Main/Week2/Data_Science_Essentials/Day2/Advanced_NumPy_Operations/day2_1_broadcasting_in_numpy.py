'''
Broadcasting in NumPy
--What is Broadcasting?
--Rules of Broadcasting
  --Dimensions are aligned from the right
        --It matches the other array's dimensions
        --One of the dimensions is 1


'''


# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a one-dimensional NumPy array
arr = np.array([1, 2, 3])

# Add the scalar value 10 to each element of the array using broadcasting
print(arr + 10)

# Create a 2x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Create a vector with 3 elements
vector = np.array([1, 0, 1])

# Add the vector to each row of the matrix using broadcasting
print(matrix + vector)

'''
Expected Output
[11 12 13]

[[2 2 4]
 [5 5 7]]
Explanation
arr + 10
NumPy broadcasts the scalar 10 to every element of the array.
Result: [1+10, 2+10, 3+10]
matrix + vector
The vector [1, 0, 1] is automatically broadcast across each row of the matrix.
Calculation:
[[1, 2, 3],      [[1, 0, 1],      [[2, 2, 4],
 [4, 5, 6]]   +   [1, 0, 1]]   =   [5, 5, 7]]

This is a classic example of NumPy broadcasting, where a smaller array is automatically expanded to match the shape of a larger array during an operation.

'''