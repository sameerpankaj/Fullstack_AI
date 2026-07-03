# Excercise 2: Regressoin Model Evaluation
#     Objective:
#         Train a regression model and evaluate its performance using MAE, MSE, and R2

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#Load Dataset
data = fetch_california_housing()
x, y = data.data, data.target

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Train Linera Regression model
model = LinearRegression()
model.fit(x_train, y_train)

#Predict
y_pred = model.predict(x_test)

#Evaluate regression metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R2 Score  (R2): {r2:.2f}')

