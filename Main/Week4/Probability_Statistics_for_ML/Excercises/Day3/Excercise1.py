#Calculate Confidence Intervals for Sample Data

import numpy as np
from scipy.stats import norm

#Generate random sample data
data = np.random.normal(loc=50, scale=10, size=100)

#Sample Statistics
mean = np.mean(data)
std = np.std(data, ddof=1)
n = len(data)

#95% Confidence Interval
z_value = norm.ppf(0.975)
margin_of_error = z_value * (std / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)

# print(f'Sample Mean: \n {mean}')
# print(f'95% Confidence Interval: \n {ci}')

print(f"Sample Mean: {mean:.2f}")
print(f"95% Confidence Interval: ({ci[0]:.2f}, {ci[1]:.2f})")