'''
Random Number Generation and Setting Seeds
--Random Number Generation
  -- np.random


'''

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Generate a 3x3 array of random floating-point numbers
# Values are randomly chosen between 0.0 and 1.0
random_array = np.random.rand(3, 3)

# Print the random array
print(f'Random Array:\n{random_array}')

# Generate a 2x3 array of random integers
# Values are randomly chosen from 0 to 9 (10 is excluded)
random_integers = np.random.randint(0, 10, size=(2, 3))

# Print the random integer array
print(f'Random Integers:\n{random_integers}')

'''
Explanation
np.random.rand(3, 3)
Creates a 3×3 array of random decimal numbers.
Each value is between 0.0 and 1.0.
np.random.randint(0, 10, size=(2, 3))
Creates a 2×3 array of random integers.
Values range from 0 to 9 because the upper bound (10) is excluded.
Sample Output
Random Array:
[[0.12 0.85 0.43]
 [0.67 0.21 0.98]
 [0.54 0.76 0.31]]

Random Integers:
[[4 7 2]
 [9 1 5]]

Note: Your output will be different each time you run the program because the numbers are generated randomly.
'''