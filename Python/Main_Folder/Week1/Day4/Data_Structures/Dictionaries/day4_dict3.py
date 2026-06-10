# Creating a dictionary with student information (key-value pairs)
student_dict = {'name': 'Alice', 'age': 25, 'grade': 'A'}

# Adding a new key-value pair to the dictionary
# 'subject' key is added with value 'Math'
student_dict['subject'] = 'Math'

# Updating an existing value
# The value of 'age' is changed from 25 to 32
student_dict['age'] = 32

# Printing the updated dictionary
print(student_dict)

# Deleting a specific key-value pair using 'del'
# This removes the key 'grade' from the dictionary permanently
del student_dict['grade']

# Printing dictionary after deletion
print(student_dict)

# Removing a key-value pair using pop()
# 'pop' removes the key 'subject' and returns its value
student_dict.pop('subject')

# Printing dictionary after pop operation
print(student_dict)