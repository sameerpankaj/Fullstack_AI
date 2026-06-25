#Poisson Distribution

import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from scipy.stats import poisson  # Import Poisson distribution

# Average number of events (λ)
lam = 3

# Generate possible event counts
x = np.arange(0, 10)

# Compute the Poisson Probability Mass Function (PMF)
y = poisson.pmf(x, lam)

# Create a bar chart
plt.bar(x, y, color='orange')

# Add title
plt.title('Poisson Distribution')

# Display the plot
plt.show()