#Calculate Probabilities Using Bayes Theorem

#- A disease affects 1% of a population
#- A test is 95% accurate for diseased individuals and 90% accurate for non-diseased individuals
#- Find the probability of having the disease given a positive test result
# Function to compute the probability of having a disease
# given a positive test result using Bayes' Theorem

def bayes_theorem(prior, sensitivity, specificity):

    # Probability of testing positive
    evidence = (sensitivity * prior) + \
               ((1 - specificity) * (1 - prior))

    # Posterior probability:
    # P(Disease | Positive Test)
    posterior = (sensitivity * prior) / evidence

    return posterior


# Disease prevalence (prior probability)
prior = 0.01  # 1%

# True positive rate
sensitivity = 0.95  # 95%

# True negative rate
specificity = 0.90  # 90%

# Compute posterior probability using Bayes' Theorem function
posterior = bayes_theorem(prior, sensitivity, specificity)

# Print the result with 4 decimal places formatting
print(f'Probability of Disease Given Positive Test: {posterior:.4f}')