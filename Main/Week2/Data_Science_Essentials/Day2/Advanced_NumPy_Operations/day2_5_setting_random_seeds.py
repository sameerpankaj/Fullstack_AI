#Setting Random Seeds

# Import the NumPy library and assign it the alias 'np'
import numpy as np

# Set the random seed to 42
# This ensures that the same random numbers are generated
# every time the program is run, making the results reproducible
np.random.seed(42)

# Generate a 3x3 array of random floating-point numbers
# Values are between 0.0 (inclusive) and 1.0 (exclusive)
random_array = np.random.rand(3, 3)

# Print the random array
print(f'Random Array:\n{random_array}')

# Generate a 2x3 array of random integers
# Values range from 0 to 9 (10 is excluded)
random_integers = np.random.randint(0, 10, size=(2, 3))

# Print the random integer array
print(f'Random Integers:\n', random_integers)




'''
Explanation
np.random.seed(42)
Sets a fixed starting point for the random number generator.
Ensures reproducible results across multiple runs.
np.random.rand(3, 3)
Creates a 3 × 3 array of random decimal numbers between 0 and 1.
np.random.randint(0, 10, size=(2, 3))
Creates a 2 × 3 array of random integers.
Values range from 0 to 9.
Expected Output

Since the seed is fixed (42), the output will always be:

Random Array:
[[0.37454012 0.95071431 0.73199394]
 [0.59865848 0.15601864 0.15599452]
 [0.05808361 0.86617615 0.60111501]]

Random Integers:
[[5 4 1]
 [7 5 1]]

Key Benefit: Setting a random seed is essential when you want your experiments, tests, or machine learning results to be reproducible.

'''