#Compute Gradients

import sympy as sp  # Import the SymPy library for symbolic mathematics

# Create symbolic variables x and y
x, y = sp.symbols('x y')

# Define the function
# f(x, y) = x² + 3y² - 4xy
f = x**2 + 3*y**2 - 4*x*y

# Compute the partial derivative with respect to x
grad_x = sp.diff(f, x)

# Compute the partial derivative with respect to y
# Note: This should be sp.diff(f, y), not sp.diff(f, x)
grad_y = sp.diff(f, y)

# Display the gradients
print('Gradients:\n')
print(f'Grad X: \n {grad_x}')
print(f'Grad Y: \n {grad_y}')