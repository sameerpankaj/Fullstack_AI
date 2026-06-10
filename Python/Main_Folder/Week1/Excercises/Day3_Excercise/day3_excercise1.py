#Create a function to calculate factorials

# Function to calculate the factorial of a number using recursion
def factorial(n):

    # Base case:
    # The factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case:
    # n! = n × (n - 1)!
    else:
        return n * factorial(n - 1)


# Function to calculate and display the factorial
def print_factorial(n):

    # Call the factorial function and store the result
    result = factorial(n)

    # Print the result using an f-string
    print(f'The factorial of {n} is {result}')


# Call the function with the value 5
print_factorial(5)

''' 
How Recursion Works

When print_factorial(5) is called:

factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1
= 120

Output:

The factorial of 5 is 120
Important Concepts

Base Case: Stops the recursion.

if n == 0 or n == 1:
    return 1

Recursive Call: The function calls itself.

return n * factorial(n - 1)
Factorial Formula:
n!=n×(n−1)!

This is a classic example of recursion in Python, where a function solves a problem by calling itself with a smaller input.
    
'''