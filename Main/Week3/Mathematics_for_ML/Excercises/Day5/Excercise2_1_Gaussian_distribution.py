#Different Probability Distributions

import numpy as np  # Numerical computations
import matplotlib.pyplot as plt  # Plotting library

from scipy.stats import norm, binom, poisson  # Statistical distributions

# -----------------------------
# Gaussian (Normal) Distribution
# -----------------------------

# Generate x values from -4 to 4
x = np.linspace(-4, 4, 100)

# Compute probability density function (PDF)
# norm.pdf = Gaussian distribution formula
y = norm.pdf(x, loc=0, scale=1)

# Plot Gaussian curve
plt.plot(x, y, label='Gaussian')

# Add title
plt.title('Gaussian Distribution')

# Display plot
plt.show()