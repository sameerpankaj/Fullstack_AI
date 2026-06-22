#Histogram

# Import the pyplot module from Matplotlib and assign it the alias 'plt'
import matplotlib.pyplot as plt

# Sample dataset
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Create a histogram
# bins=4 divides the data range into 4 intervals (bins)
# color='green' sets the color of the bars
# edgecolor='black' adds black borders around each bar
plt.hist(data, bins=4, color='green', edgecolor='black')

# Add a title to the histogram
plt.title('Histogram')

# Display the histogram
plt.show()


'''
Explanation
Dataset
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

Frequency of each value:

Value	Frequency
1	1
2	2
3	3
4	4
Creating the Histogram
plt.hist(data, bins=4, color='green', edgecolor='black')
plt.hist() creates a histogram.
bins=4 divides the data into 4 intervals.
color='green' fills the bars with green.
edgecolor='black' draws black borders around the bars.
What a Histogram Shows

A histogram displays the distribution of numerical data.

For this dataset:

Value  Frequency
1      *
2      **
3      ***
4      ****

The value 4 occurs most frequently, while 1 occurs least frequently.

Visual Representation

The histogram will resemble:

Frequency
4 |           █
3 |        █  █
2 |     █  █  █
1 |  █  █  █  █
   +------------
     1  2  3  4
Enhanced Version
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4, color='green', edgecolor='black')

plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.show()
Key Concept

A histogram is used to:

Understand data distribution
Identify patterns and trends
Detect skewness
Spot outliers
Analyze frequencies of values

Unlike a bar chart, which compares categories, a histogram groups continuous numerical data into ranges (bins) and shows how often values fall within those ranges.


'''
