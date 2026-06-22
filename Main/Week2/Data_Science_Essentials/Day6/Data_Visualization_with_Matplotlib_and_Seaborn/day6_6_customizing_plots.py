#customizing plots

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

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend(['Dataset 1'])



# Display the plot
plt.show()