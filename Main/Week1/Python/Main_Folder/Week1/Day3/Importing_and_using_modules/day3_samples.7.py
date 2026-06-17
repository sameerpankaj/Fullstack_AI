#creating custom modules

'''
Example 1: Simple Math Module
Step 1: Create a file named mymath.py
# mymath.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
Step 2: Use the module in another file
# main.py

import mymath

print(mymath.add(5, 3))
print(mymath.multiply(5, 3))

Output:

8
15
Example 2: Import Specific Functions
Module: calculator.py
# calculator.py

def square(num):
    return num * num

def cube(num):
    return num * num * num
Main Program
from calculator import square

print(square(4))

Output:

16
Example 3: Module with Variables
Module: config.py
# config.py

APP_NAME = "Jarvis AI"
VERSION = "1.0"
Main Program
import config

print(config.APP_NAME)
print(config.VERSION)

Output:

Jarvis AI
1.0
Example 4: Module with Functions and Variables
Module: student.py
# student.py

school_name = "ABC School"

def get_student_name():
    return "Sameer"

def get_grade():
    return "A"
Main Program
import student

print(student.school_name)
print(student.get_student_name())
print(student.get_grade())

Output:

ABC School
Sameer
A
Example 5: Using an Alias
Module: mymath.py
def add(a, b):
    return a + b
Main Program
import mymath as mm

print(mm.add(10, 20))

Output:

30
Example 6: Module for Your Jarvis Project
musicLibrary.py
# musicLibrary.py

songs = {
    "believer": "https://youtube.com/example1",
    "shapeofyou": "https://youtube.com/example2",
    "perfect": "https://youtube.com/example3"
}
main.py
import musicLibrary

print(musicLibrary.songs["believer"])

Output:

https://youtube.com/example1
Folder Structure
Project/
│
├── main.py
├── mymath.py
├── calculator.py
└── musicLibrary.py

Python can import these modules because they are in the same folder as main.py.

Key Rule

A custom module is simply a Python file (.py) that you create and then import into another Python file.

For example:

# greetings.py

def say_hello():
    print("Hello!")
# main.py

import greetings

greetings.say_hello()

Output:

Hello!

This is the simplest and most common pattern for creating custom modules in Python.
'''