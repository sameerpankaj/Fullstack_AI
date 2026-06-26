#Simulate Dice Rolls and Calculate Probabilities

# Import the NumPy library for numerical operations and random number generation.
import numpy as np

# Simulate 10,000 rolls of a six-sided dice.
# np.random.randint(1, 7) generates random integers from 1 to 6
# (the upper limit 7 is not included).
rolls = np.random.randint(1, 7, size=10000)

# Calculate the probability of rolling an even number.
# rolls % 2 == 0 creates a Boolean array where:
# True = even number
# False = odd number
# np.sum() counts the number of True values.
# Divide by the total number of rolls to get the probability.
P_even = np.sum(rolls % 2 == 0) / len(rolls)

# Calculate the probability of rolling a number greater than 4.
# rolls > 4 creates a Boolean array where:
# True = 5 or 6
# False = 1, 2, 3, or 4
# Count the True values and divide by the total number of rolls.
P_greater_than_4 = np.sum(rolls > 4) / len(rolls)

# Display the estimated probability of rolling an even number.
print(f'P(Even): \n {P_even}')

# Display the estimated probability of rolling a number greater than 4.
print(f'P(Greater than 4): \n {P_greater_than_4}')