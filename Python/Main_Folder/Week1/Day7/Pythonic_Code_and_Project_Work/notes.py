'''
Writing Clean, 'Pythonic' Code
--What is pythonic code?
Pythonic code means writing code in a way that follows Python's philosophy and conventions—code that is simple, readable, elegant, and efficient.

Python programmers often refer to the principles in the "Zen of Python":

import this

Some famous lines are:

Beautiful is better than ugly.
Simple is better than complex.
Readability counts.

Example 1: Looping Through a List
Non-Pythonic
fruits = ["apple", "banana", "orange"]

for i in range(len(fruits)):
    print(fruits[i])
Pythonic
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

The Pythonic version is shorter and easier to read.

Example 2: Checking for Membership
Non-Pythonic
found = False

for fruit in fruits:
    if fruit == "apple":
        found = True
        break

if found:
    print("Found")
Pythonic
if "apple" in fruits:
    print("Found")
Example 3: Creating a List
Non-Pythonic
squares = []

for i in range(10):
    squares.append(i ** 2)
Pythonic
squares = [i ** 2 for i in range(10)]

This is called a list comprehension.

Example 4: Swapping Variables
Non-Pythonic
temp = a
a = b
b = temp
Pythonic
a, b = b, a
Example 5: Opening Files
Non-Pythonic
file = open("data.txt", "r")
content = file.read()
file.close()
Pythonic
with open("data.txt", "r") as file:
    content = file.read()

This automatically closes the file.



--Best Practices
  use descriptive variable names
  wirte modular code with functions and classes
  Follwo PEP 8 style guidilines
  Avoid reducndancy; leverate pythons pwoerfule built ins




List Comprehnesions
--What are list comprehesions?
  --A concise way to create lists using a single line of code




#Lambda Functions
--What are lambda functions?
A lambda function is a small, anonymous (unnamed) function that can be written in a single line.

Syntax
lambda arguments: expression

It's equivalent to a normal function that returns a value.

Example 1: Simple Addition
Normal Function
def add(a, b):
    return a + b
Lambda Function
add = lambda a, b: a + b

print(add(5, 3))  # 8
Example 2: Square a Number
square = lambda x: x ** 2

print(square(4))  # 16

Equivalent to:

def square(x):
    return x ** 2
Common Use Case: sorted()

Suppose you have a list of tuples:

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

Sort by marks:

students.sort(key=lambda student: student[1])

print(students)

Output:

[
    ('Charlie', 78),
    ('Alice', 85),
    ('Bob', 92)
]

Here:

lambda student: student[1]

means:

"Take a student tuple and return the second element (the marks)."

Common Use Case: map()
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)

Output:

[1, 4, 9, 16]
Common Use Case: filter()
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

Output:

[2, 4, 6]
Limitations of Lambda Functions

A lambda can contain only one expression.

❌ Not allowed:

lambda x:
    y = x + 1
    return y

For multiple statements, use a normal function:

def process(x):
    y = x + 1
    return y
When to Use Lambda

✅ Short, simple functions used once
✅ sorted(), map(), filter()
✅ Passing a function as an argument

❌ Complex logic
❌ Multiple statements
❌ When readability suffers

Pythonic Alternative

Many Python developers prefer list comprehensions over map() and filter():

numbers = [1, 2, 3, 4]

squares = [x ** 2 for x in numbers]

instead of:

squares = list(map(lambda x: x ** 2, numbers))

Both work, but the list comprehension is often considered more readable.


map(), filter(), and reduce()
--map()
    --Applies a function to each item in an iterable
--filter()
    --Filters items based on a condition
--reduce()
    --Reduces an iterable to a single value




Python's os and sys Modules
--os Module
    --Provides functions to interact with the operating system
--sys Module
    --Provides access to system specific parameters and functions

    
  


'''