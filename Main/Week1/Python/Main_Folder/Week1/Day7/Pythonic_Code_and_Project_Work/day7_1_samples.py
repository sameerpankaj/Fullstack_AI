#[expression for item in iterable if condition]

#Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

#Filter Even numbers
evens = [x for x in range(100) if x % 2 == 0]
print(evens)