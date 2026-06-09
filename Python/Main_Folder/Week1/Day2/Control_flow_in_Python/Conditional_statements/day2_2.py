#Example 2: Nested conditions
# Infinite loop - keeps running until the user types 'quit'
while True:

    # Ask the user to enter an age or quit
    age = input("Enter age (or 'quit' to exit): ")

    # Check if the user wants to exit the program
    if age.lower() == 'quit':
        print("Program terminated.")
        break  # Exit the loop

    # Convert the input from string to integer
    age = int(age)

    # Check if the age is invalid (negative)
    if age < 0:
        print('Invalid age')

    # Check if the age is less than 18
    elif age < 18:
        print('Minor')

    # Check if the age is between 18 and 29
    elif age < 30:
        print('Young adult')

    # If age is 30 or above
    else:
        print('Adult')

        '''
Example Run
Enter age (or 'quit' to exit): 15
Minor

Enter age (or 'quit' to exit): 25
Young adult

Enter age (or 'quit' to exit): 40
Adult

Enter age (or 'quit' to exit): -5
Invalid age

Enter age (or 'quit' to exit): quit
Program terminated.

'''