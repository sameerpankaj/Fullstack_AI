#Implement a Simple Linear Regression Model Using Scikit-Learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


#Generate synthetic Data
np.random.seed(42)
x = np.random.rand(100, 1) * 100
y = 3 * x * np.random.randn(100, 1) * 2

#Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Fit linear regression
model = LinearRegression()
model.fit(x_train, y_train)

#Make predictinos
y_pred = model.predict(x_test)

# print coefficeints
print('Slope: ', model.coef_[0][0])
print('Intercept :', model.intercept_[0])