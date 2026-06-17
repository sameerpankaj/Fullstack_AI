#filter()
# Create a list of numbers
numbers = [1, 2, 3, 4]

# Use filter() to keep only the numbers that satisfy the condition
# lambda x: x % 2 == 0 checks if a number is even
# If the condition is True, the number is included in the result
# filter() returns a filter object (an iterator)
evenList = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object to a list and print the even numbers
print(list(evenList))

'''
Step-by-step execution
numbers = [1, 2, 3, 4]

For each number, the lambda function checks:

lambda x: x % 2 == 0
1 % 2 == 0 → False ❌
2 % 2 == 0 → True ✅
3 % 2 == 0 → False ❌
4 % 2 == 0 → True ✅

So filter() keeps only:

2, 4

When converted to a list:

print(list(evenList))

Output:

[2, 4]
Pythonic Alternative

Many Python developers prefer a list comprehension:

numbers = [1, 2, 3, 4]

# Create a list containing only even numbers
evenList = [x for x in numbers if x % 2 == 0]

print(evenList)

Output:

[2, 4]

'''