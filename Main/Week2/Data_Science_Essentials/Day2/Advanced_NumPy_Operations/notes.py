'''
Broadcasting in NumPy
--What is Broadcasting?
--Rules of Broadcasting
  --Dimensions are aligned from the right
        --It matches the other array's dimensions
        --One of the dimensions is 1


Aggregation functions
--aggregation fumctions compute summary statistics for arrays
--common functions


Boolean Indexing and Filtering
--What is Boolean Indexing?


Random Number Generation and Setting Seeds
--Random Number Generation
  -- np.random
--Setting Random Seeds






'''

'''
Broadcasting in NumPy

Broadcasting is a feature in NumPy that allows arrays of different shapes to work together in arithmetic operations without explicitly resizing them.

It automatically stretches the smaller array to match the shape of the larger array when possible.

Example 1: Scalar Broadcasting
import numpy as np

arr = np.array([1, 2, 3, 4])

# Add 10 to every element in the array
result = arr + 10

print(result)
Output
[11 12 13 14]

Here, NumPy automatically broadcasts the scalar 10 to:

[10 10 10 10]

and performs element-wise addition.

Example 2: Broadcasting with Arrays
import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

vector = np.array([10, 20, 30])

result = matrix + vector

print(result)
Output
[[11 22 33]
 [14 25 36]]

NumPy treats the vector as:

[[10 20 30]
 [10 20 30]]

and adds it to each row of the matrix.

Broadcasting Rules

NumPy compares shapes from right to left:

Dimensions are equal, or
One of the dimensions is 1

If neither condition is met, broadcasting fails.

Example
(2, 3)
(1, 3)

Broadcasting works because:

3 == 3
1 can be stretched to 2

Result shape:

(2, 3)
Example of an Error
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([1, 2])

print(a + b)
Error
ValueError: operands could not be broadcast together

Shapes:

a -> (2, 3)
b -> (2,)

Comparing from the right:

3 != 2

So broadcasting is not possible.

Why Broadcasting is Useful
Makes code shorter and cleaner.
Avoids creating unnecessary copies of data.
Improves performance and memory efficiency.
Widely used in data science, machine learning, and numerical computing.

In simple terms: Broadcasting lets NumPy perform operations on arrays of different sizes by automatically expanding the smaller array when the shapes are compatible.
'''