'''
What is NumPy?
--Numerical Python
Why Use Numpy in AI?
--Performance
--Ease of Use
--Integration

'''

'''

NumPy (short for Numerical Python) is a popular Python library used for fast mathematical and scientific computing. It provides a powerful data structure called an array, which is more efficient than Python lists for numerical operations.

Why use NumPy?
Faster computations than regular Python lists
Supports multi-dimensional arrays (vectors, matrices, tensors)
Includes many mathematical functions
Widely used in data science, machine learning, and scientific computing
Installation
pip install numpy
Basic Example
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

print(arr)

Output:

[1 2 3 4 5]
Array Operations
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Element-wise addition
print(a * b)  # Element-wise multiplication

Output:

[5 7 9]
[ 4 10 18]
Matrix Example
import numpy as np

matrix = np.array([[1, 2],
                   [3, 4]])

print(matrix)

Output:

[[1 2]
 [3 4]]
Common NumPy Functions
np.zeros((2, 3))   # Array of zeros
np.ones((2, 3))    # Array of ones
np.arange(0, 10)   # Numbers 0 to 9
np.mean(arr)       # Average
np.sum(arr)        # Sum
np.max(arr)        # Maximum value
Where NumPy is Used
Data analysis (with Pandas)
Machine learning (with Scikit-learn)
Deep learning (with TensorFlow and PyTorch)
Scientific simulations
Image and signal processing

Think of NumPy as the foundation of numerical computing in Python—if you're working with numbers, matrices, or data, NumPy is often the first library you'll use.
'''