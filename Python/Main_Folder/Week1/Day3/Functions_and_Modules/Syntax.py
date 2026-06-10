'''
Defining Functions with def

What are Functions?
Functions in Python

A function is a reusable block of code that performs a specific task. Functions help make your code organized, reusable, and easier to maintain.

Defining a Function

Use the def keyword to create a function:

# Define a function
def greet():
    print("Hello, World!")

# Call the function
greet()

Output:

Hello, World!
Function with Parameters

Parameters allow you to pass data into a function.

# Function with one parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Sameer")

Output:

Hello, Sameer!
Function with Multiple Parameters
# Function that adds two numbers
def add(a, b):
    print(a + b)

add(10, 5)

Output:

15
Function Returning a Value

Use return to send a value back to the caller.

# Function that returns the sum
def add(a, b):
    return a + b

result = add(10, 5)
print(result)

Output:

15
Default Parameters

You can provide default values for parameters.

# Function with a default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Sameer")

Output:

Hello, Guest!
Hello, Sameer!
Function with No Return Statement

If a function doesn't return anything, it returns None.

def hello():
    print("Hello")

result = hello()
print(result)

Output:

Hello
None
Example: Even or Odd Function
# Check whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(8))

Output:

Even
Why Use Functions?
Avoid repeating code
Make programs easier to read
Simplify debugging
Break large problems into smaller tasks
Improve code reusability
Example from Your Calculator Program
# Function to multiply two numbers
def mul(a, b):
    return a * b

result = mul(4, 5)
print(result)

Output:

20

Think of a function like a machine:

Input → Parameters
Processing → Function body
Output → Return value

For example:

def square(num):
    return num * num

print(square(5))

Input: 5 → Function → Output: 25


'''

