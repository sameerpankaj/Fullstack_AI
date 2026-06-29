# ----------------------------------------------------
# Perform a One-Sample Hypothesis Test (One-Sample t-test)
# ----------------------------------------------------

# Import required libraries
import numpy as np
from scipy.stats import ttest_1samp

# ----------------------------------------------------
# Step 1: Define the sample data
# These are the observed sample values.
# ----------------------------------------------------
data = [12, 14, 15, 16, 17, 18, 19]

# ----------------------------------------------------
# Step 2: Define the null hypothesis
# H0 (Null Hypothesis): The population mean is 15.
# H1 (Alternative Hypothesis): The population mean is not 15.
# ----------------------------------------------------
population_mean = 15

# ----------------------------------------------------
# Step 3: Perform a one-sample t-test
# ttest_1samp() compares the sample mean with
# the hypothesized population mean.
#
# It returns:
#   t_stat  -> Test statistic
#   p_value -> Probability of obtaining the observed
#               result if the null hypothesis is true.
# ----------------------------------------------------
t_stat, p_value = ttest_1samp(data, population_mean)

# ----------------------------------------------------
# Step 4: Display the test results
# ----------------------------------------------------
print(f'T-Statistic:\n{t_stat}')
print(f'P-Value:\n{p_value}')

# ----------------------------------------------------
# Step 5: Set the significance level (alpha)
# A common choice is 0.05 (5% significance level).
# ----------------------------------------------------
alpha = 0.05

# ----------------------------------------------------
# Step 6: Interpret the results
#
# If p-value <= alpha:
#     Reject the null hypothesis.
#     There is statistically significant evidence that
#     the population mean differs from 15.
#
# If p-value > alpha:
#     Fail to reject the null hypothesis.
#     There is not enough evidence to conclude that
#     the population mean differs from 15.
# ----------------------------------------------------
if p_value <= alpha:
    print("Reject the null hypothesis: Significant difference exists.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")