#Bar Chart

# Import the pyplot module from Matplotlib and assign it the alias 'plt'
import matplotlib.pyplot as plt

# Categories for the x-axis
categories = ['A', 'B', 'C']

# Corresponding values for each category
values = [10, 15, 7]

# Create a bar chart
# Each category gets a bar whose height corresponds to its value
plt.bar(categories, values, color='blue')

# Add a title to the chart
plt.title('Bar Chart')

# Display the chart
plt.show()


'''
Explanation
Data
Category	Value
A	10
B	15
C	7
Creating the Bar Chart
plt.bar(categories, values, color='blue')
categories are placed on the x-axis.
values determine the height of each bar.
color='blue' makes all bars blue.
Visual Representation
Bar Chart

Comparison of values for categories A, B, and C.

0
4
8
12
16
A
B
C
Why Use a Bar Chart?

Bar charts are useful for:

Comparing categories
Showing rankings
Visualizing counts or frequencies
Highlighting differences between groups
Enhanced Version
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C']
values = [10, 15, 7]

plt.bar(categories, values, color='blue')

plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()

This version adds labels to both axes, making the chart easier to interpret.


'''