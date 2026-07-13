#Apply Regularization

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error

#Load dataset
california = fetch_california_housing()
x, y = california.data, california.target
feature_names = california.feature_names

#split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display dataset info
print('Feature names:\n', feature_names)
print('\n Sample Data:\n', pd.DataFrame(x, columns=feature_names).head())

#Train Linear Regression model without regularizatoin
lr_model = LinearRegression()
lr_model.fit(x_train, y_train)

#Predict and evaluate
y_pred = lr_model.predict(x_test)
mse_lr = mean_squared_error(y_test, y_pred)

print(f'Linear Regression MSE (No Regularization): {mse_lr:.2f}')
print('Coefficients:\n', lr_model.coef_)

#Train Ridge regression model
ridge_model = Ridge(alpha=0.1)
ridge_model.fit(x_train, y_train)

#Predict and evaluate 
y_pred_ridge = ridge_model.predict(x_test)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)

print(f'Ridge Regression MSE: {mse_ridge:.2f}')
print('Coefficients: \n', ridge_model.coef_)
