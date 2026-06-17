#sys module

# Import the built-in sys module
# It provides access to Python interpreter variables and functions
import sys

# Print the list of command-line arguments
# sys.argv is a list where:
# argv[0] = name/path of the Python script
# argv[1], argv[2], ... = arguments passed to the script
print(sys.argv)

# Print information about the Python version currently running
# Includes version number, build information, and compiler details
print(sys.version)

'''
Example

Suppose your script is named example.py and you run:

python example.py hello 123

Then:

print(sys.argv)

Output:

['example.py', 'hello', '123']

Explanation:

'example.py' → script name
'hello' → first argument
'123' → second argument

And:

print(sys.version)

might output something like:

3.13.5 (tags/v3.13.5:abc123, May 10 2026, 12:00:00)
[MSC v.1944 64 bit (AMD64)]
Beginner-Friendly Version
import sys

# Display all command-line arguments passed to the script
print(sys.argv)

# Display the Python interpreter version being used
print(sys.version)

Tip: sys.argv is commonly used when you want users to provide input while running a Python program from the command line. For example:

python calculator.py 10 20

Your program can then access 10 and 20 through sys.argv.

'''