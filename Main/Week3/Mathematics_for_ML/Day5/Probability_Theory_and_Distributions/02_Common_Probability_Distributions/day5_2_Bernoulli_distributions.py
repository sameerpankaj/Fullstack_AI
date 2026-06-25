#Bernoulli Distributions

import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Probability of success
p = 0.6

# Create a bar chart for the Bernoulli distribution
# P(X=0) = 1 - p (Failure)
# P(X=1) = p     (Success)
plt.bar([0, 1], [1 - p, p], color='blue')

# Add a title to the plot
plt.title('Bernoulli Distribution')

# Label the x-axis categories
# Note: The first argument should be [0, 1], not [1, 1]
plt.xticks([0, 1], labels=['0 (Failure)', '1 (Success)'])

# Display the plot
plt.show()