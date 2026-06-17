#adding dimension to arrays

import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3])

# Add a new axis to convert the 1D array into a column vector
expanded = arr[:, np.newaxis]

# Print the expanded array
print(expanded)

'''
Output
[[1]
 [2]
 [3]]

'''


