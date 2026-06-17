
#This program is same as day3_excercise1 but in this program the user is inputing its own number

# Function to calculate the factorial of a number using recursion
def factorial(n):

    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n × (n - 1)!
    else:
        return n * factorial(n - 1)


# Function to calculate and print the factorial
def print_factorial(n):

    # Calculate the factorial
    result = factorial(n)

    # Display the result
    print(f'The factorial of {n} is {result}')


# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and print the factorial
    print_factorial(num)

'''
Example Run
Enter a number: 5
The factorial of 5 is 120
Enter a number: 0
The factorial of 0 is 1
Enter a number: -3
Factorial is not defined for negative numbers.

The factorial relationship being used is:

n!=n×(n−1)!

with the base cases 0! = 1 and 1! = 1.

'''