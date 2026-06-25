#Task 1: Implement the Mathematical Formula for linear regression

import numpy as np

#Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

#Add bias term to feature matrix
X_b = np.c_[np.ones((100, 1)), X]

#Initialize parameters
theta = np.random.randn(2, 1)
learning_rate = 0.1
iteration = 1000

#

def predict(X, theta):
    return np.dot(X, theta)


#Task2:Use Gradient Descent to Optimize the Model Parameters

def gradient_descent(X, y, theta, learning_rate, iteration):
    m = len(y)
    for _ in range(iteration):
        gradients = (1/m) * np.dot(X.T, (np.dot(X, theta) - y))
        theta -= learning_rate *gradients
    return theta

#Task3: Calculate Evaluation Metrics

def mean_square_error(y_true, y_predicted_values):
    return np.mean((y_true - y_predicted_values))

def r_squared(y_true, y_predicted_values):
    ss_res = np.sum((y_true - y_predicted_values) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

#Perform gradient descent
theta_optimized = gradient_descent(X_b, y, theta, learning_rate, iteration)

#Predictions and evaluations
y_prediction = predict(X_b, theta_optimized)
mse = mean_square_error(y, y_prediction)
r_square = r_squared(y, y_prediction)

print(f'Optimized Parameters (Theta): \n {theta_optimized}')
print(f'MSE: \n {mse}')
print(f'R square: \n {r_square}')

