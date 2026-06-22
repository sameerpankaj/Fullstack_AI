#Basic Syntax

# Import the pyplot module from Matplotlib and assign it the alias 'plt'
import matplotlib.pyplot as plt

# Create data for the x-axis
x = [1, 2, 3, 4]

# Create corresponding data for the y-axis
y = [10, 20, 25, 30]

# Create a basic line plot
# Matplotlib connects the data points with lines
plt.plot(x, y)

# Display the plot window
plt.show()


'''
Explanation
import matplotlib.pyplot as plt
Imports Matplotlib's plotting module.
plt is the standard alias used for plotting.
x = [1, 2, 3, 4]
Defines the values for the x-axis.
y = [10, 20, 25, 30]
Defines the values for the y-axis.
plt.plot(x, y)
Creates a line chart using the x and y values.
Points plotted:
(1, 10)
(2, 20)
(3, 25)
(4, 30)
plt.show()
Displays the chart in a new window.
What the Graph Looks Like

The graph shows a line connecting the points:

30 |                *
25 |           *
20 |      *
10 | *
   +-------------------
     1   2   3   4
Enhanced Version
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)

plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

'''