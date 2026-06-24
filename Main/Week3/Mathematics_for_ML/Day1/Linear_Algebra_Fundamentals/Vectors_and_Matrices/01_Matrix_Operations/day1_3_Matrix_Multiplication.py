
# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create two 2×2 matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Perform matrix multiplication
result = np.dot(A, B)

# Display the result
print(f'Matrix Multiplication:\n{result}')



'''

Matrix multiplication is different from normal element-wise multiplication.

When multiplying two matrices, you multiply rows of the first matrix by columns of the second matrix and add the results.

Rule
(AB)
11
	​

=20
Row
1
2
Column
1
2
(AB)
11
	​

=(2⋅5)+(1⋅1)+(3⋅3)=20
A
2
1
3
4
0
2
×
B
5
2
1
4
3
7
=
AB
20
29
26
22
(2 × 5) + (1 × 1) + (3 × 3) = 20
Example

Let:

A=[
1
3
	​

2
4
	​

]
B=[
5
7
	​

6
8
	​

]

To find the first element of AB:

(1×5)+(2×7)=5+14=19

To find the second element:

(1×6)+(2×8)=6+16=22

To find the third element:

(3×5)+(4×7)=15+28=43

To find the fourth element:

(3×6)+(4×8)=18+32=50

Result:

AB=[
19
43
	​

22
50
	​

]
NumPy Example
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = A @ B

print(result)

Output:

[[19 22]
 [43 50]]
Difference Between * and @
A * B

Output (element-wise multiplication):

[[ 5 12]
 [21 32]]

because:

1×5 = 5
2×6 = 12
3×7 = 21
4×8 = 32

Whereas:

A @ B

Output (matrix multiplication):

[[19 22]
 [43 50]]
Summary
Operation	NumPy Symbol	Result
Element-wise multiplication	A * B	Multiply matching elements
Matrix multiplication	A @ B or np.dot(A, B)	Row × Column multiplication

In machine learning and data science, matrix multiplication (@) is one of the most important operations because it is used in neural networks, linear regression, image processing, and many other algorithms.
'''