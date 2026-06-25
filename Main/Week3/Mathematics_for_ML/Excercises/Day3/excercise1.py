#Compute Derivatives fo Basic Functions

import sympy as sp  # Import the SymPy library for symbolic mathematics

# Create a symbolic variable X
x = sp.Symbol('X')

# Define the function f(X) = X³ - 5X + 7
f = x**3 - 5*x + 7

# Compute the derivative of f with respect to X
derivative = sp.diff(f, x)

# Display the function
print(f'Function: \n {f}')

# Display the derivative
print(f'Derivative: \n {derivative}')