import numpy as np

#Random variable: dice roll
outcomes = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.array([1/6] * 6)

#Expectation
expectation = np.sum(outcomes * probabilities)
print(f'Expectation (mean): \n {expectation}')


#Variance and standard deviation
variance = np.sum((outcomes - expectation) ** 2 * probabilities)
std_dev = np.sqrt(variance)
print(f'Variance: \n {variance}')
print(f'Standard Deviation: {std_dev}')
