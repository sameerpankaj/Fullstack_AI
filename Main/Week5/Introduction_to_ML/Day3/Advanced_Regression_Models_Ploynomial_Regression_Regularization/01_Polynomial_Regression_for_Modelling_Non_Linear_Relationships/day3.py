import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Generate Synthetic Data
np.random.seed(42)
x = np.random.rand(100, 1) * 10
y = 3 * x**2 + np.random.randn(100, 1) * 5

# Transform features to polynomial
poly_features = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly_features.fit_transform(x)

#Fit Polynomial Regression
model = LinearRegression()
model.fit(x_poly, y)
y_pred = model.predict(x_poly)

#Plot results
plt.scatter(x, y, color='blue', label='Actual Data')
plt.scatter(x, y_pred, color='red', label='Predicted Data')
plt.title('Polynomial Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#Evaluate Model
mse = mean_squared_error(y, y_pred)
print('Mean Square Error (MSE): ', mse)