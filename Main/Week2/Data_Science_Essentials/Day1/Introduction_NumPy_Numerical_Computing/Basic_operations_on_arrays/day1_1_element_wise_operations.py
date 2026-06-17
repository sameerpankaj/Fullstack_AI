#element wise operations on arrays

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create the first NumPy array
a = np.array([1, 2, 3])

# Create the second NumPy array
b = np.array([4, 5, 6])

# Perform element-wise addition and print the result
print(a + b)

# Perform element-wise multiplication and print the result
print(a * b)

# Perform element-wise division and print the result
print(a / b)


'''

Output
[5 7 9]
[ 4 10 18]
[0.25       0.4        0.5       ]
Explanation
a + b adds corresponding elements: (1+4), (2+5), (3+6)
a * b multiplies corresponding elements: (1×4), (2×5), (3×6)
a / b divides corresponding elements: (1÷4), (2÷5), (3÷6)

These are called element-wise operations because NumPy performs the operation on each pair of elements at the same index.


'''