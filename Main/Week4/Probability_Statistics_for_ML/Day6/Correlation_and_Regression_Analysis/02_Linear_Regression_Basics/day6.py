import numpy as np
from sklearn.linear_model import LinearRegression


#Sample Data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 8, 10])

'Fit Liear Regression'
model = LinearRegression()
model.fit(x, y)

print('Slope: \n', model.coef_[0])
print('Itercept: \n', model.intercept_)
print('R-Squared: \n', model.score(x,y))