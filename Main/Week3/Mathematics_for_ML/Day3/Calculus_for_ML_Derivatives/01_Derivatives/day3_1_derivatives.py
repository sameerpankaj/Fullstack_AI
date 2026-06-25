import sympy as sp  # Import the SymPy library for symbolic mathematics

# Create a symbolic variable x
# Note: It is conventional to use a lowercase symbol name
x = sp.Symbol('x')

# Define the function f(x) = x²
f = x**2

# Compute the derivative of f with respect to x
derivative = sp.diff(f, x)

# Display the derivative
print(f'Derivative: \n {derivative}')