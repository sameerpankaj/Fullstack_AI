# Use lasso and Ridge Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split

#Load the california housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

#Select Feature(Median Income) and target (Median house value)
x = df[['MedInc']]
y = df[['MedHouseVal']]


#Transform feature to polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly.fit_transform(x)

#Split data into training and testing sets
x_train, x_test , y_train, y_test = train_test_split(x_poly, y, test_size=0.2, random_state=4)


#Ridge Regression
ridge_model = Ridge(alpha=1)
ridge_model.fit(x_train, y_train)
ridge_predictions = ridge_model.predict(x_test)

#lasso regression
lasso_model = Lasso(alpha=1)
lasso_model.fit(x_train, y_train)
lasso_predictions = lasso_model.predict(x_test)

#Evaluate Ridge Regression
ridge_mse = mean_squared_error(y_test, ridge_predictions)
print('Ridge Regressoin MSE: ', ridge_mse)

#Evaluate Ridge Regression
lasso_mse = mean_squared_error(y_test, lasso_predictions)
print('Lasso Regressoin MSE: ', lasso_mse)

#Plot Ridge vs Lasso values
plt.figure(figsize=(10, 6))
plt.scatter(x_test[:, 0], y_test, color='blue', label='Actual Data', alpha=0.5 )
plt.scatter(x_test[:, 0], ridge_predictions, color='green', label='Ridge Predictions', alpha=0.5)
plt.scatter(x_test[:, 0], lasso_predictions, color='orange', label='Lasso Predictions', alpha=0.5)
plt.title('Ridge vs Lasso Regression')
plt.xlabel('Median Income Transformed')
plt.ylabel('Median House value in California')
plt.legend()
plt.show()


