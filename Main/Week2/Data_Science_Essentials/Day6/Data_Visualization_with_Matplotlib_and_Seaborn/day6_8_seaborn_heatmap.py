# Import the pyplot module from Matplotlib
import matplotlib.pyplot as plt

# Import Seaborn for advanced statistical visualizations
import seaborn as sns

# Import NumPy for numerical operations
import numpy as np

# Generate a 5x5 array of random numbers between 0 and 1
data = np.random.rand(5, 5)

# Create a heatmap
# annot=True displays the numerical value in each cell
# cmap='coolwarm' applies a color gradient from cool to warm colors
sns.heatmap(data, annot=True, cmap='coolwarm')

# Add a title to the heatmap
plt.title('HeatMap')

# Display the heatmap
plt.show()


'''
Explanation
Generate Random Data
data = np.random.rand(5, 5)

Creates a 5 × 5 matrix of random decimal values:

Example:

[[0.37 0.95 0.73 0.60 0.16]
 [0.16 0.06 0.87 0.60 0.71]
 [0.02 0.97 0.83 0.21 0.18]
 [0.18 0.30 0.52 0.43 0.29]
 [0.61 0.14 0.29 0.37 0.46]]
Create a Heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')

Parameters:

data
The matrix to visualize.
annot=True
Displays the numerical values inside each cell.
cmap='coolwarm'
Applies a color scheme:
Blue → Lower values
White → Medium values
Red → Higher values
What is a Heatmap?

A heatmap represents data using colors.

Low Values  → Blue
Medium      → White
High Values → Red

This makes it easy to spot patterns, trends, and extreme values.

Typical Uses of Heatmaps
Correlation matrices
Machine learning analysis
Data exploration
Performance metrics
Feature relationships
Enhanced Version
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(42)

data = np.random.rand(5, 5)

sns.heatmap(
    data,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Random Data HeatMap')
plt.show()
Additional Parameter
fmt='.2f'

Displays numbers with 2 decimal places, making the heatmap cleaner and easier to read.

Sample Visualization

A heatmap might look like:

+------+------+------+------+
| 0.37 | 0.95 | 0.73 | 0.60 |
| 0.16 | 0.06 | 0.87 | 0.60 |
| 0.02 | 0.97 | 0.83 | 0.21 |
| 0.18 | 0.30 | 0.52 | 0.43 |
| 0.61 | 0.14 | 0.29 | 0.46 |
+------+------+------+------+

with the cells colored from blue to red according to their values. This visual representation makes it much easier to identify high and low values than reading the numbers alone.


'''