# Create Basic Plots with Matplotlib

import matplotlib.pyplot as plt

# Data for the line plot
years = [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]

# Create a line plot
plt.plot(
    years,
    sales,
    label='Sales Trend',
    color='blue',
    marker='o'
)

# Add labels to the axes
plt.xlabel('Years')
plt.ylabel('Sales')

# Display the legend
plt.legend()

# Display the plot
plt.show()


'''
Explanation
Data
Year	Sales
2010	100
2011	120
2012	140
2013	160
Visual Representation
Sales Trend

Sales growth from 2010 to 2013.

75
100
125
150
175
2010
2011
2012
2013
Understanding the Code
plt.plot()
plt.plot(
    years,
    sales,
    label='Sales Trend',
    color='blue',
    marker='o'
)
years → values on the x-axis.
sales → values on the y-axis.
label='Sales Trend' → text shown in the legend.
color='blue' → line color.
marker='o' → displays a circle at each data point.
plt.xlabel('Years')

Labels the horizontal axis as Years.

plt.ylabel('Sales')

Labels the vertical axis as Sales.

plt.legend()

Displays a legend showing:

Sales Trend
plt.show()

Renders and displays the chart.

What the Graph Shows

The chart indicates a steady increase in sales:

2010 → 100
2011 → 120
2012 → 140
2013 → 160

This suggests a consistent upward sales trend over the four-year period.


'''