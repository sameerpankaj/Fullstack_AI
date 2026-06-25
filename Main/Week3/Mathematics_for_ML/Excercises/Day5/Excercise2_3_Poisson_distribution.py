#Different Probability Distributions

import numpy as np  # Numerical computations
import matplotlib.pyplot as plt  # Plotting library

from scipy.stats import norm, binom, poisson  # Statistical distributions

#Poisson distribution
lam = 3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, label='Poisson')
plt.title('Poisson Distribution')
plt.show()