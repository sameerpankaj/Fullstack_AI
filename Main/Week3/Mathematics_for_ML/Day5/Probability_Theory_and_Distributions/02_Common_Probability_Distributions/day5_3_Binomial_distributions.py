#Binomial Distribution

import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from scipy.stats import binom  # Import Binomial distribution from SciPy

# Number of trials (n) and probability of success (p)
n, p = 10, 0.5

# Generate possible numbers of successes: 0, 1, ..., 10
x = np.arange(0, n + 1)

# Compute the probability mass function (PMF)
# PMF gives P(X = x) for each possible number of successes
y = binom.pmf(x, n, p)

# Create a bar chart of the binomial probabilities
plt.bar(x, y, color='green')

# Add a title to the plot
plt.title('Binomial Distribution')

# Display the plot
plt.show()