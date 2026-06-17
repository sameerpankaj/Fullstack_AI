'''
Lists in Python

A list is a collection of items stored in a single variable.

Lists can store:

Numbers
Strings
Booleans
Other lists
Mixed data types
Creating a List
# A list of fruits
fruits = ["apple", "banana", "orange"]

print(fruits)

Output:

['apple', 'banana', 'orange']
Accessing List Elements

Lists use indexing, starting from 0.

fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

Output:

apple
banana
orange
Negative Indexing

Negative indexes start from the end.

fruits = ["apple", "banana", "orange"]

print(fruits[-1])

Output:

orange
Modifying List Elements
fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)

Output:

['apple', 'mango', 'orange']
Adding Elements
append()

Adds an item to the end of the list.

fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)

Output:

['apple', 'banana', 'orange']
Inserting Elements
insert()
fruits = ["apple", "banana"]

fruits.insert(1, "mango")

print(fruits)

Output:

['apple', 'mango', 'banana']
Removing Elements
remove()
fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)

Output:

['apple', 'orange']
Removing by Index
pop()
fruits = ["apple", "banana", "orange"]

fruits.pop(1)

print(fruits)

Output:

['apple', 'orange']
Length of a List
fruits = ["apple", "banana", "orange"]

print(len(fruits))

Output:

3
Looping Through a List
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

Output:

apple
banana
orange
Check if an Item Exists
fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("Found!")

Output:

Found!
Sorting a List
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)

Output:

[1, 2, 5, 8]
Reversing a List
numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)

Output:

[4, 3, 2, 1]
List of Mixed Data Types
data = ["Sameer", 25, True, 5.5]

print(data)

Output:

['Sameer', 25, True, 5.5]
List Slicing

Get a portion of a list.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

Output:

[20, 30, 40]
Taking List Input from the User
# Ask the user to enter numbers separated by spaces
numbers = input("Enter numbers separated by spaces: ").split()

print(numbers)

Input:

10 20 30 40

Output:

['10', '20', '30', '40']

To convert them to integers:

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)

Output:

[10, 20, 30, 40]
Example Program: Find the Largest Number
# Create a list of numbers
numbers = [10, 25, 5, 40, 15]

# Find the largest number
largest = max(numbers)

print(f"The largest number is {largest}")

Output:

The largest number is 40
Summary

A list is:

Ordered
Mutable (can be changed)
Allows duplicate values
Uses square brackets []

Example:

my_list = [1, 2, 3, 4, 5]

Lists are one of the most important data structures in Python and are used extensively in AI, data science, automation, and general programming.

You’re out of messages with the most advanc

'''