# Import the Matplotlib library for creating graphs and visualizations.
import matplotlib.pyplot as plt

# Import the uniform distribution from the SciPy statistics module.
# This provides functions such as the Probability Density Function (PDF).
from scipy.stats import uniform

# Import the NumPy library for numerical operations.
import numpy as np

# Continuous Random Variable: Uniform Distribution

# Generate 100 equally spaced values between 0 and 1.
# These values represent the x-axis points for the distribution.
x = np.linspace(0, 1, 100)

# Calculate the Probability Density Function (PDF) values
# for a Uniform distribution on the interval [0, 1].
# loc = 0   -> starting point of the distribution
# scale = 1 -> width of the distribution (1 - 0 = 1)
pdf = uniform.pdf(x, loc=0, scale=1)

# Plot the PDF as a red line graph.
plt.plot(x, pdf, color='red')

# Add a title to the graph.
plt.title('PDF of Uniform(0,1)')

# Label the x-axis.
plt.xlabel('X')

# Label the y-axis (Probability Density Function values).
plt.ylabel('f(X)')

# Display the graph.
plt.show()