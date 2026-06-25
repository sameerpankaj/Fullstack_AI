#Common probability distributions

import numpy as np  # Import NumPy for numerical computations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Mean (μ) and standard deviation (σ) of the Gaussian distribution
mu, sigma = 0, 1

# Generate 100 equally spaced points between -4 and 4
x = np.linspace(-4, 4, 100)

# Compute the Gaussian (Normal) Distribution PDF
# Formula:
# f(x) = (1 / √(2πσ²)) * exp(-(x-μ)² / (2σ²))
y = (1 / (np.sqrt(2 * np.pi * sigma**2))) * \
    np.exp(-0.5 * ((x - mu) / sigma)**2)

# Plot the Gaussian curve
plt.plot(x, y)

# Add a title to the graph
plt.title('Gaussian Distribution')

# Display the graph
plt.show()

