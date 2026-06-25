import scipy.stats as stats  # Import SciPy statistics module

# Sample dataset
data = [10, 20, 30, 40, 50]

# -----------------------------
# Mean
# -----------------------------
mean = sum(data) / len(data)

# -----------------------------
# Variance (population variance)
# -----------------------------
variance = sum((x - mean) ** 2 for x in data) / len(data)

# -----------------------------
# Standard Deviation
# -----------------------------
standard_deviation = variance ** 0.5

# -----------------------------
# Confidence Interval (95%)
# -----------------------------
sample_mean = mean

# Z-score for 95% confidence
z_score = 1.96

confidence_interval = (
    sample_mean - z_score * (standard_deviation / len(data) ** 0.5),
    sample_mean + z_score * (standard_deviation / len(data) ** 0.5)
)

# Print result
print(f'Confidence Interval: \n {confidence_interval}')