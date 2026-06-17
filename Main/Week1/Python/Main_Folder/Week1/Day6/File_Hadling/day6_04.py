'''
--Basic Exception Handling for File operations
    Prevents the program form crashing due to file related errors (eg, file not found)
--Using try except block
--Common File Handling Exceptions
  FileNotFoundError
  PermissionError
  IOError    thats is Input Output Error
'''


with open('sample1.txt', 'w') as file:
    file.write('Hello World')
    file.writelines(['Alice', 'Bob', 'Cherry'])


try:
    with open('sample.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found')