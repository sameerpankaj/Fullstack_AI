#Scatter Plot

# Import the pyplot module from Matplotlib and assign it the alias 'plt'
import matplotlib.pyplot as plt

# Data points for the x-axis
x = [1, 2, 3, 4, 5]

# Data points for the y-axis
y = [10, 12, 25, 30, 45]

# Create a scatter plot
# Each (x, y) pair is displayed as an individual point
plt.scatter(x, y, color='red')

# Add a title to the plot
plt.title('Scatter Plot')

# Display the plot
plt.show()


'''
Explanation
Data Points

The scatter plot displays the following points:

X	Y
1	10
2	12
3	25
4	30
5	45
Creating the Scatter Plot
plt.scatter(x, y, color='red')
plt.scatter() creates a scatter plot.
Each (x, y) pair is plotted as a separate dot.
color='red' makes all points red.
What the Plot Shows

Points plotted:

Y
45 |                ●
40 |
35 |
30 |            ●
25 |        ●
20 |
15 |
12 |    ●
10 | ●
   +--------------------
     1  2  3  4  5    X

Unlike a line plot, the points are not connected by lines.

Why Use a Scatter Plot?

Scatter plots are useful for:

Finding relationships between variables
Detecting trends
Identifying clusters
Spotting outliers
Exploring correlations

For example, in this dataset:

As X increases, Y also increases.

This suggests a positive correlation between X and Y.

Enhanced Version
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]

plt.scatter(x, y, color='red')

plt.title('Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')

plt.show()

Adding axis labels makes the chart easier to understand and interpret.


'''