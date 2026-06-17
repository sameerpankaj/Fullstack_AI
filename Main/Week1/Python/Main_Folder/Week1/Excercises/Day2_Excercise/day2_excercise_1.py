#Write a program to check if the number is a prime number

# Ask the user to enter a number and convert the input to an integer
num = int(input('Enter a number: '))

# Prime numbers must be greater than 1
if num > 1:

    # Check for factors from 2 up to the square root of the number
    # Using square root improves efficiency because factors always come in pairs
    for i in range(2, int(num ** 0.5) + 1):

        # If the number is divisible by i, it is not prime
        if num % i == 0:
            print(f'{num} is not a prime number')
            break  # Exit the loop as soon as a factor is found

    # This else belongs to the for loop
    # It executes only if the loop completes without finding a factor
    else:
        print(f'{num} is a prime number')

# Numbers less than or equal to 1 are not prime
else:
    print(f'{num} is not a prime number')

'''
How it works

For num = 17:

Check divisibility by 2, 3, and 4 (√17 ≈ 4.12)
No factor is found
The for loop finishes normally
The else block runs
Output:
17 is a prime number

For num = 12:

Check divisibility by 2
12 % 2 == 0
A factor is found
break executes
Output:
12 is not a prime number

Important: The else after a for loop is a special Python feature. It runs only if the loop completes without hitting a break.

'''