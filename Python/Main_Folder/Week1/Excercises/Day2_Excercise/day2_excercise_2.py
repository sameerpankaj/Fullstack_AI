#Create a Menu Driven Calculator

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def mul(a, b):
    return a * b

# Function to divide the first number by the second
def divide(a, b):

    # Check if the divisor is not zero
    if b != 0:
        return a / b
    else:
        # Return an error message if division by zero is attempted
        return 'Division by zero is not allowed'


# Infinite loop to keep the calculator running
while True:

    # Display the calculator menu
    print('\nMenu:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')

    # Get the user's choice
    choice = input('Enter your choice: ')

    # Exit the program if the user chooses option 5
    if choice == '5':
        print('Exiting program')
        break

    # Get two numbers from the user
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    # Perform addition if the user selects option 1
    if choice == '1':
        print('Result:', add(num1, num2))

    # Perform subtraction if the user selects option 2
    elif choice == '2':
        print('Result:', subtract(num1, num2))

    # Perform multiplication if the user selects option 3
    elif choice == '3':
        print('Result:', mul(num1, num2))

    # Perform division if the user selects option 4
    elif choice == '4':
        print('Result:', divide(num1, num2))

    # Handle invalid menu choices
    else:
        print('Invalid choice. Please try again')

'''
Program Overview

This is a menu-driven calculator that:

Adds two numbers
Subtracts two numbers
Multiplies two numbers
Divides two numbers
Prevents division by zero
Runs continuously until the user selects 5 (Exit)

'''