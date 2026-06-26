# Import the product function from the itertools module.
# (Note: It is not used in this program, so this import can be removed.)
from itertools import product

# Create the sample space for a single six-sided dice roll.
# The possible outcomes are 1, 2, 3, 4, 5, and 6.
sample_space = list(range(1, 7))

# List all the even numbers that can appear on the dice.
even_numbers = [2, 4, 6]

# Calculate the probability of rolling an even number.
# Probability = Number of favorable outcomes / Total number of possible outcomes
P_even = len(even_numbers) / len(sample_space)

# Display the probability of rolling an even number.
print(f'P(Even): \n {P_even}')
