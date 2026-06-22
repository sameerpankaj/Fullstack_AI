'''
Introduction to Matplotlib for Plotting
--What is Matplotlib?
--Basic Syntax

Bsaic Plots
--Line Plot
--Bar Chart
--Histogram
--Scatter Plot



Customizing Plots
--Add titles, axis labels, and legends
--Adjust colors and styles



Introduction to Seaborn for Advanced Visualizations
--What is seaborn
--common seaborn plots
  --heatmap
  --Pairplot
  



'''


'''
Matplotlib in Python

Matplotlib is a popular Python library used for data visualization. It helps you create charts, graphs, and plots to visually represent data.

It is one of the most widely used visualization libraries in Python and works very well with NumPy and Pandas.

Why Use Matplotlib?
Create line charts
Create bar charts
Create pie charts
Create histograms
Create scatter plots
Visualize trends and patterns in data
Present data in an easy-to-understand format
Installing Matplotlib
pip install matplotlib
Importing Matplotlib
import matplotlib.pyplot as plt

The alias plt is the standard convention.

Simple Line Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)

plt.title("Simple Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
What Happens?
plt.plot(x, y) creates a line graph.
plt.title() adds a title.
plt.xlabel() labels the x-axis.
plt.ylabel() labels the y-axis.
plt.show() displays the chart.
Bar Chart
import matplotlib.pyplot as plt

students = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 88]

plt.bar(students, scores)

plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")

plt.show()

A bar chart is useful for comparing categories.

Scatter Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()

A scatter plot helps visualize relationships between variables.

Histogram
import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 30]

plt.hist(data)

plt.title("Histogram")

plt.show()

A histogram shows the distribution of data.

Pie Chart
import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++']
sizes = [50, 30, 20]

plt.pie(sizes, labels=labels)

plt.title("Programming Language Popularity")

plt.show()

A pie chart shows proportions of a whole.

Plotting Data from Pandas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Sales': [100, 150, 120]
})

plt.plot(df['Month'], df['Sales'])

plt.title("Monthly Sales")
plt.show()
Common Matplotlib Functions
Function	Purpose
plt.plot()	Line chart
plt.bar()	Bar chart
plt.scatter()	Scatter plot
plt.hist()	Histogram
plt.pie()	Pie chart
plt.title()	Add title
plt.xlabel()	Label x-axis
plt.ylabel()	Label y-axis
plt.legend()	Show legend
plt.grid()	Show grid
plt.show()	Display plot
Relationship with NumPy and Pandas
NumPy      → Numerical computations
Pandas     → Data analysis and manipulation
Matplotlib → Data visualization
Example
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = x ** 2

plt.plot(x, y)
plt.title("y = x²")
plt.show()

This creates a graph of the mathematical function y = x².

Summary

Matplotlib is Python's foundational plotting library. It allows you to transform raw data into visual charts and graphs, making it easier to identify trends, patterns, comparisons, and insights. It is commonly used alongside NumPy and Pandas in data science, machine learning, analytics, and scientific computing.


'''