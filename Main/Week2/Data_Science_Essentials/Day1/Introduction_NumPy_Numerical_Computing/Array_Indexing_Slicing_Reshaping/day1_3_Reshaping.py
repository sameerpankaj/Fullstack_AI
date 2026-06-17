#Reshaping arrays


# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Create a NumPy array with 6 elements
arr = np.array([10, 20, 30, 40, 50, 60])

# Reshape the 1D array into a 2D array with 2 rows and 3 columns
reshaped = arr.reshape(2, 3)

# Print the reshaped array
print(reshaped)