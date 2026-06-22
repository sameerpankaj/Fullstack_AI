import matplotlib.pyplot as plt

#Bar Chart
categories = ['Electronics', 'Clothing', 'Groceries']
revenue = [250, 400, 150]
plt.bar(categories, revenue, color='green')
plt.title('Revenue by Category')
plt.show()