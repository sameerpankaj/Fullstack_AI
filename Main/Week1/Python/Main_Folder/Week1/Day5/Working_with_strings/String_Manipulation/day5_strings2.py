#Slicing 

# Creating the first string
first = 'Hello'

# Creating the second string
second = 'World'

# Concatenating (joining) the two strings with a space in between
result = first + ' ' + second

# Creating a string for demonstrating slicing
text = 'Python Programming'

# Slicing from index 0 to 5 (6 is excluded)
# This extracts the word 'Python'
print(text[0:6])

# Using negative indexing to slice the last 11 characters
# This extracts the word 'Programming'
print(text[-11:])


'''
Output:
Python
Programming
'''