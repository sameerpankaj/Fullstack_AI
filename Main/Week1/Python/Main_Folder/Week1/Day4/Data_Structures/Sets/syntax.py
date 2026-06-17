'''

A set in Python is an unordered collection of unique elements.
It is used when you want to store items without duplicates.

🔹 Creating a Set
# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Set with mixed data types
mixed_set = {1, "apple", True}

⚠️ Important:

Sets use { }
But empty {} is NOT a set (it is a dictionary)
Empty set is created using set()
empty_set = set()
🔹 No Duplicates Allowed
nums = {1, 2, 2, 3, 3, 4}
print(nums)   # Output: {1, 2, 3, 4}
🔹 Adding Elements
fruits = {"apple", "banana"}

fruits.add("orange")   # add one item
print(fruits)
🔹 Removing Elements
fruits = {"apple", "banana", "orange"}

fruits.remove("banana")  # removes banana
# fruits.discard("banana") # safer alternative (no error if not found)

print(fruits)
🔹 Set Operations
Union (combine sets)
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # {1, 2, 3, 4, 5}
Intersection (common elements)
print(A & B)   # {3}
Difference
print(A - B)   # {1, 2}
🔹 Looping Through a Set
for item in {10, 20, 30}:
    print(item)
🔥 Key Features of Sets
Unordered (no index)
No duplicate values
Mutable (can add/remove items)
Very fast for membership testing
📊 Real-Life Example

Think of a set like:

A list of unique usernames
A list of unique email IDs

'''