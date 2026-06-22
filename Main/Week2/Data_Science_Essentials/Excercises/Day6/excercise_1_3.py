# Create Basic Plots with Matplotlib

import matplotlib.pyplot as plt

# Data for the scatter plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]

# Create a scatter plot
plt.scatter(hours_studied, exam_scores, color='red')

# Add title and axis labels
plt.title('Study Hours vs Exam Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')

# Display the plot
plt.show()


'''
Explanation
Data
Hours Studied	Exam Score
1	50
2	55
3	65
4	70
5	85
Understanding the Code
plt.scatter()
plt.scatter(hours_studied, exam_scores, color='red')
Creates a scatter plot.
Each pair of values becomes a point:
(1, 50)
(2, 55)
(3, 65)
(4, 70)
(5, 85)
color='red' makes all points red.
Title
plt.title('Study Hours vs Exam Scores')

Adds a title at the top of the chart.

X-axis Label
plt.xlabel('Hours Studied')

Labels the horizontal axis.

Y-axis Label

Your code currently has:

plt.ylabel('Hours Studied')

This is a small mistake. The y-axis represents exam scores, so it should be:

plt.ylabel('Exam Scores')
What the Plot Shows

The scatter plot suggests a positive relationship between study time and exam performance:

More Hours Studied → Higher Exam Scores

As the number of study hours increases from 1 to 5, exam scores generally increase from 50 to 85.

Key Concept

Scatter plots are commonly used to:

Find relationships between two variables
Detect trends
Identify clusters
Spot outliers
Analyze correlations

In this example, the plot indicates that students who study more tend to score higher on the exam.


'''