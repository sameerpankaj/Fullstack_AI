import numpy as np  # Import NumPy for numerical computations

# Dataset
data = [10, 20, 30, 40, 50]

# -----------------------------
# Mean
# -----------------------------
mean = np.mean(data)

# -----------------------------
# Variance (population variance)
# -----------------------------
variance = np.var(data)

# -----------------------------
# Standard Deviation
# -----------------------------
standard_deviation = np.std(data)

# -----------------------------
# Print results
# -----------------------------
print(f'Mean: \n {mean}')
print(f'Variance: \n {variance}')
print(f'Standard Deviation: \n {standard_deviation}')