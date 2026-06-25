#Calculate Integrals fo Simple Functions

import sympy as sp

#Define a function
x = sp.Symbol('x')
f = sp.exp(-x)

#Compute indefinite integral
indefinite_integral = sp.integrate(f, x)
print(f'Indefinite integral: \n {indefinite_integral}')


#Compute definite integral
definite_integral = sp.integrate(f, (x, 0, sp.oo))
print(f'Definite integral: \n {definite_integral}')