#Line Plot

# Import the pyplot module from Matplotlib and assign it the alias 'plt'
import matplotlib.pyplot as plt

# Create a line plot
# x-values: [1, 2, 3]
# y-values: [10, 20, 30]
# label is used to identify the line in the legend
plt.plot([1, 2, 3], [10, 20, 30], label='Trend')

# Add a title to the chart
plt.title('Line Plot')

# Label the x-axis
plt.xlabel('X-axis')

# Label the y-axis
plt.ylabel('Y-axis')

# Display the legend using the label provided in plt.plot()
plt.legend()

# Display the chart
plt.show()



'''
Explanation
Creating the Line Plot
plt.plot([1, 2, 3], [10, 20, 30], label='Trend')

Plots the points:

X	Y
1	10
2	20
3	30

and connects them with a line.

The argument:

label='Trend'

gives the line a name that will appear in the legend.

Adding a Title
plt.title('Line Plot')

Displays the title at the top of the chart.

Labeling Axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

Adds descriptive labels to the horizontal and vertical axes.

Displaying the Legend
plt.legend()

Shows a legend box containing:

Trend

This is especially useful when a chart contains multiple lines.

What the Graph Represents

The graph shows a steadily increasing trend:

30 |              *
25 |
20 |       *
15 |
10 | *
   +----------------
     1   2   3

The line rises from 10 to 30, indicating a positive trend.

Key Concept

A line plot is commonly used to visualize:

Trends over time
Growth or decline
Continuous data
Comparisons between multiple data series

The label and legend() combination is important when plotting multiple lines on the same graph.


'''