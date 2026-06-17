# List slicing and basic list operations in Python

# A list of integers
numbers = [1, 2, 3, 4]

# A list of strings (fruits)
fruits = ['Apple', 'Banana', 'Cherry']

# A mixed list containing different data types
mixed_list = [1, 'apple', True]

# Accessing list elements using index (commented examples)
# print(numbers[3])   # prints the 4th element (index starts from 0)
# print(fruits[0])    # prints the first element: Apple
# print(mixed_list[1])# prints 'apple'
# print(fruits[-1])   # negative indexing: prints last element → Cherry

# Adding an element at the end of the list
fruits.append('orange')  
# Now 'orange' is added after 'Cherry'

# Inserting an element at a specific position
fruits.insert(1, 'grape')  
# Inserts 'grape' at index 1 (shifts other elements to the right)

# Printing the updated list
print(fruits)

# Slicing the list (extracting part of the list)
sliced_fruits = fruits[1:3]  
# Gets elements from index 1 to 2 (3 is excluded)

# Printing the sliced portion
print(sliced_fruits)