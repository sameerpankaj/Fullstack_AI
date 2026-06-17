'''
What are Modules?

Modules in Python

A module is a Python file (.py) that contains functions, variables, and classes that can be reused in other Python programs.

Think of a module as a toolbox containing useful code that you can import whenever you need it.

Why Use Modules?
Reuse code across multiple programs
Organize large projects
Avoid writing the same code repeatedly
Access Python's built-in functionality
Importing a Module

Python comes with many built-in modules.

Example: math Module
import math

print(math.sqrt(25))
print(math.pi)

Output:

5.0
3.141592653589793
Import Specific Functions

Instead of importing the entire module, you can import only what you need.

from math import sqrt, pi

print(sqrt(16))
print(pi)

Output:

4.0
3.141592653589793
Using an Alias

You can give a module a shorter name.

import math as m

print(m.sqrt(36))

Output:

6.0
Creating Your Own Module
Step 1: Create a file named calculator.py
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
Step 2: Use the module in another file
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))

Output:

15
5
Import Specific Functions from Your Module
from calculator import add

print(add(20, 10))

Output:

30
The __name__ Variable

When a file is run directly, Python sets __name__ to "__main__".

def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()

This is commonly used to run test code only when the file is executed directly.

Useful Built-in Modules
Module	Purpose
math	Mathematical functions
random	Random numbers and selections
os	Interact with the operating system
sys	Python system functions
datetime	Date and time handling
json	Working with JSON data
time	Time-related functions
Example: Random Module
import random

print(random.randint(1, 10))

This prints a random number between 1 and 10.

Example Related to Your Jarvis Project

You already have:

import musicLibrary

This means musicLibrary.py is a custom module that contains code you want to reuse.

For example:

musicLibrary.py

songs = {
    "believer": "https://..."
}

main.py

import musicLibrary

print(musicLibrary.songs)

Here, musicLibrary is your own module, and main.py imports and uses it.

Summary
A module is a .py file containing reusable code.
Use import module_name to import a module.
Use from module_name import item to import specific items.
Python provides many built-in modules like math, random, and datetime.
You can create your own modules by saving functions and variables in a separate .py file.

'''