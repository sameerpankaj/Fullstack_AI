#os module
# Import the built-in os module
# It provides functions for interacting with the operating system
import os

# Print the current working directory function object
# NOTE: This is missing parentheses, so it prints the function itself,
# not the actual current directory path.
print(os.getcwd)

# Create a new directory (folder) named 'test_dir'
# Raises FileExistsError if the directory already exists.
os.mkdir('test_dir')

# Delete the file named 'file.txt'
# Raises FileNotFoundError if the file does not exist.
os.remove('file.txt')

'''
Correction

If your goal is to print the current working directory, you should call the function:

import os

# Print the current working directory path
print(os.getcwd())

# Create a new directory named 'test_dir'
os.mkdir('test_dir')

# Delete the file named 'file.txt'
os.remove('file.txt')
Example Output

If your current directory is:

C:\Full_Stack_AI\Python

then:

print(os.getcwd())

would output:

C:\Full_Stack_AI\Python

Whereas:

print(os.getcwd)

would output something like:

<built-in function getcwd>

because you're printing the function object itself rather than calling it.

'''