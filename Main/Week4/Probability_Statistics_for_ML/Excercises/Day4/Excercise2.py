# ----------------------------------------------------
# Perform a Two-Sample t-Test (Independent Samples t-Test)
# ----------------------------------------------------

# Import the required libraries
import numpy as np
from scipy.stats import ttest_ind

# ----------------------------------------------------
# Step 1: Define the data for two independent groups
# These are the sample observations from Group 1 and Group 2.
# ----------------------------------------------------
group1 = [12, 14, 15, 16, 17, 18, 19]
group2 = [11, 13, 14, 15, 16, 17, 18]

# ----------------------------------------------------
# Step 2: Perform an independent two-sample t-test
#
# H0 (Null Hypothesis):
#     The means of the two groups are equal.
#
# H1 (Alternative Hypothesis):
#     The means of the two groups are different.
#
# ttest_ind() returns:
#     t_stat  -> Test statistic
#     p_value -> Probability of obtaining the observed
#                difference if the null hypothesis is true.
# ----------------------------------------------------
t_stat, p_value = ttest_ind(group1, group2)

# ----------------------------------------------------
# Step 3: Display the test results
# ----------------------------------------------------
print(f'T-Statistic:\n{t_stat}')
print(f'P-Value:\n{p_value}')

# ----------------------------------------------------
# Step 4: Set the significance level (alpha)
# A significance level of 0.05 (5%) is commonly used.
# ----------------------------------------------------
alpha = 0.05

# ----------------------------------------------------
# Step 5: Interpret the results
#
# If p-value <= alpha:
#     Reject the null hypothesis.
#     There is a statistically significant difference
#     between the means of the two groups.
#
# If p-value > alpha:
#     Fail to reject the null hypothesis.
#     There is not enough evidence to conclude that
#     the group means are different.
# ----------------------------------------------------
if p_value <= alpha:
    print("Reject the null hypothesis: Significant difference exists.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")


    '''
What this test is used for

A Two-Sample t-Test (Independent Samples t-Test) is used to determine whether the means of two independent groups are significantly different. For example:

Comparing the exam scores of two different classes.
Comparing the average heights of men and women.
Comparing the average sales of two different stores.

'''