# Import the pyplot module from Matplotlib and assign it the alias 'plt'
import matplotlib.pyplot as plt

# Create a line plot with custom styling
plt.plot(
    [1, 2, 3],          # X-values
    [10, 20, 30],       # Y-values
    label='Trend',      # Label for the legend
    color='orange',     # Line color
    linestyle='--',     # Dashed line style
    marker='o'          # Circle marker at each data point
)

# Add a title to the chart
plt.title('Line Plot')

# Label the x-axis
plt.xlabel('X-axis')

# Label the y-axis
plt.ylabel('Y-axis')

# Display the legend
plt.legend()

# Display the chart
plt.show()


'''
Explanation
color='orange'
color='orange'
Changes the color of the line to orange.
Other common colors:
'red'
'blue'
'green'
'black'
'purple'
linestyle='--'
linestyle='--'

Controls the appearance of the line.

Common styles:

Style	Meaning
'-'	Solid line
'--'	Dashed line
':'	Dotted line
'-.'	Dash-dot line
marker='o'
marker='o'

Adds a marker at each data point.

Common markers:

Marker	Shape
'o'	Circle
's'	Square
'^'	Triangle
'*'	Star
'x'	Cross
Data Being Plotted
X	Y
1	10
2	20
3	30
Visual Representation

The chart would look approximately like this:

30 |                  o
25 |
20 |         o
15 |
10 | o
   +--------------------
      1     2     3

The points are connected by an orange dashed line, and each point is marked with a circle (o).

Result

This example demonstrates how to customize a line plot by controlling:

Color (color)
Line style (linestyle)
Data point markers (marker)
Legend (label + legend())

These options make charts more informative and visually appealing.


'''
