#Different Probability Distributions

import numpy as np  # Numerical computations
import matplotlib.pyplot as plt  # Plotting library

from scipy.stats import norm, binom, poisson  # Statistical distributions

# Binomial Distribution
# n = number of trials, p = probability of success
n, p = 10, 0.5

# Possible outcomes: 0 to n successes
x = np.arange(0, n + 1)

# PMF (Probability Mass Function) for Binomial distribution
# Gives probability of exactly k successes in n trials
y = binom.pmf(x, n, p)

# Plot bar chart for binomial distribution
plt.bar(x, y, label='Binomial')

# Add title
plt.title('Binomial Distribution')

# Display plot
plt.show()