#Create and Analyze Random Variables

# Import the Matplotlib library for creating graphs and charts.
import matplotlib.pyplot as plt

# Import the uniform distribution from SciPy.
# Note: It is not used in this program and can be removed.
from scipy.stats import uniform

# Define the possible outcomes of rolling a fair six-sided dice.
outcomes = [1, 2, 3, 4, 5, 6]

# Define the probability of each outcome.
# Since the dice is fair, each outcome has a probability of 1/6.
# [1/6] * 6 creates a list containing six values of 1/6.
probabilities = [1/6] * 6

# Create a bar chart representing the Probability Mass Function (PMF)
# of a fair six-sided dice.
plt.bar(outcomes, probabilities, color='blue', alpha=0.7)

# Add a title to the graph.
plt.title('PMF of a Dice Roll')

# Label the x-axis with the possible outcomes.
plt.xlabel('Outcomes')

# Label the y-axis with the probabilities.
plt.ylabel('Probability')

# Display the graph.
plt.show()