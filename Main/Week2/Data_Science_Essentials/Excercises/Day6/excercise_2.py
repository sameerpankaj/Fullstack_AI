# Create a Heatmap with Seaborn
#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv


# Import Pandas for data handling
import pandas as pd

# Import Seaborn for visualization (heatmap)
import seaborn as sns

# Import Matplotlib for plotting controls
import matplotlib.pyplot as plt

# Load the Iris dataset from an online CSV file
df = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
)

# Remove the 'species' column because correlation works only on numeric data
del df['species']

# Calculate the correlation matrix for all numeric columns
# This shows how strongly variables are related to each other
correlation_matrix = df.corr()

# Create a heatmap to visualize correlations
# annot=True → shows numeric values inside cells
# cmap='coolwarm' → color scale from low (cool) to high (warm)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Add a title to the heatmap
plt.title('Correlation Heatmap')

# Display the plot
plt.show()


'''
Key Explanation
Correlation matrix (df.corr())
Measures relationships between numeric features
Values range from:
+1 → strong positive correlation
0 → no correlation
-1 → strong negative correlation
Heatmap
Visual representation of the correlation matrix
Makes patterns easy to spot quickly
Important Fixes in Your Code
coorelation_matrix → corrected to correlation_matrix
Corelation Heatmap → should be Correlation Heatmap

This is a standard data science workflow:
Load data → clean → compute correlation → visualize with heatmap


'''