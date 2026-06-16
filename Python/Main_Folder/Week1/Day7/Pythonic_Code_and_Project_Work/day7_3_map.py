#map()

# Create a list of numbers
numbers = [1, 2, 3, 4]

# Use map() to apply the lambda function to each element in the list
# lambda x: x**2 takes a number x and returns its square
# map() returns a map object (an iterator)
squares = map(lambda x: x**2, numbers)

# Convert the map object to a list and print the result
print(list(squares))