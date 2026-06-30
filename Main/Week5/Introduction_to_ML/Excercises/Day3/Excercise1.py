#Implement polynomial Regression and visualize the fit

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Load the california housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

#Select Feature(Median Income) and target (Median house value)
x = df[['MedInc']]
y = df[['MedHouseVal']]


#Transform feature to polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly.fit_transform(x)

#Fit Polynomial regression model
model = LinearRegression()
model.fit(x_poly, y)

#Make predictions
y_pred = model.predict(x_poly)

#Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Actual Data', alpha=0.5 )
plt.scatter(x, y_pred, color='red', label='Predicted Curve', alpha=0.5)
plt.title('Polynomial Regression')
plt.xlabel('Median Income in California')
plt.ylabel('Median House value in California')
plt.legend()
plt.show()