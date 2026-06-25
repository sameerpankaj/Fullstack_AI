import sympy as sp  # Import the SymPy library for symbolic mathematics

# Create symbolic variables x and y
x, y = sp.symbols('x y')

# Define the function f(x, y) = x² + y²
f = x**2 + y**2

# Compute the partial derivative with respect to x
grad_x = sp.diff(f, x)

# Compute the partial derivative with respect to y
grad_y = sp.diff(f, y)

# Display the partial derivatives
print(f'Partial Derivatives: \n {(grad_x, grad_y)}')