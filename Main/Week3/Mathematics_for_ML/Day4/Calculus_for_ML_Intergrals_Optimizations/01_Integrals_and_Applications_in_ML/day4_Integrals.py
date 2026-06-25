#Integrals and their applications in ML

import sympy as sp  # Import the SymPy library for symbolic mathematics

# Create a symbolic variable X
x = sp.Symbol('X')

# Define the function f(X) = X²
f = x**2

# Compute the definite integral of f from X = 0 to X = 2
definite_integral = sp.integrate(f, (x, 0, 2))

# Compute the indefinite integral of f
indefinite_integral = sp.integrate(f, x)

# Display the results
print(f'Definite Integral: \n {definite_integral}')
print(f'Indefinite Integral: \n {indefinite_integral}')