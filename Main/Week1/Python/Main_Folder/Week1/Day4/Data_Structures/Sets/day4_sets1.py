# Creating a set of numbers
numbers = {1, 2, 3, 4}

# Creating an empty set (IMPORTANT: use set(), not {})
empty_set = set()

# Printing the original set
print(numbers)

# Adding a new element to the set
numbers.add(5)
print(numbers)

# Trying to add a duplicate element
# Sets do not allow duplicates, so 4 will not be added again
numbers.add(4)

# Printing set after attempting to add duplicate
print(numbers)