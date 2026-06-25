#Variance

from statistics import mode

# A simple dataset (list of numbers)
data = [10, 20, 30, 40, 50]

# -----------------------------
# Mean (Average)
# -----------------------------
# Mean = sum of all values / number of values
mean = sum(data) / len(data)

# Display mean
print(f'Mean: \n {mean}')

# -----------------------------
# Median
# -----------------------------
# Step 1: Sort the data (important for median)
sorted_data = sorted(data)

# Step 2: Find middle value
# If number of elements is odd → pick middle element
# If even → average of two middle elements
median = (
    sorted_data[len(data) // 2]
    if len(data) % 2 != 0
    else (
        sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]
    ) / 2
)

# Display median
print(f'Median: \n {median}')

# Display mode
print(f'Mode: \n {mode(data)}')

# Compute variance using the formula (population variance)

variance = sum((x - mean) ** 2 for x in data) / len(data)

# Display variance
print(f'Variance: \n {variance}')