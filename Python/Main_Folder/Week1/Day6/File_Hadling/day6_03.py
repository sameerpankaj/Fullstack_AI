'''
--Using 'with' statements for File Management
  What is the with statement?
In Python, the with statement is used to work with resources (like files, database connections, locks, etc.) and automatically clean them up when you're done.

Basic Syntax
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
What happens here?
open("sample.txt", "r") opens the file.
as file stores the file object in the variable file.
The code inside the with block executes.
When the block ends, Python automatically closes the file—even if an error occurs.

This is equivalent to:

file = open("sample.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()
Why use with?

✅ Automatically releases resources
✅ Prevents forgetting to close files
✅ Handles exceptions safely
✅ Makes code cleaner and more readable

Example: Writing to a File
with open("sample.txt", "w") as file:
    file.write("Hello, Python!")

After the block ends, sample.txt is automatically closed.

In your earlier file-handling example

If you do:

with open("sample.txt", "w") as file:
    file.write("Hello")

Python will:

Create sample.txt if it doesn't exist (because of "w" mode).
Open it for writing.
Write "Hello".
Automatically close the file when the block finishes.

That's one of the main reasons with is considered the preferred way to work with files in Python.


'''