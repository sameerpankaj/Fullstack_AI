'''
Tuples in Python

A tuple is a built-in data type in Python used to store multiple items in a single variable, just like a list.
But the key difference is: tuples are immutable (cannot be changed after creation).

🔹 Creating a Tuple
# empty tuple
t1 = ()

# tuple with integers
t2 = (1, 2, 3, 4)

# tuple with mixed data types
t3 = (1, "apple", True)

# tuple without parentheses (also valid)
t4 = 10, 20, 30
🔹 Accessing Elements
fruits = ("apple", "banana", "cherry")

print(fruits[0])   # apple
print(fruits[-1])  # cherry (last element)
🔹 Tuple Slicing
numbers = (1, 2, 3, 4, 5)

print(numbers[1:4])  # (2, 3, 4)
🔹 Why Tuples are Immutable
t = (1, 2, 3)

# t[0] = 10  ❌ This will give an error

Once created, you cannot:

add elements
remove elements
change values
🔹 Tuple Methods (limited)
t = (1, 2, 3, 2, 2)

print(t.count(2))  # 3 → counts occurrences of 2
print(t.index(3))  # 2 → position of value 3
🔹 Tuple vs List
Feature	List	Tuple
Syntax	[ ]	( )
Changeable	Yes	No
Speed	Slower	Faster
Methods	Many	Few
🔹 When to use Tuples?

Use tuples when:

Data should not change (e.g., coordinates, dates)
You want faster performance
You want data safety


'''