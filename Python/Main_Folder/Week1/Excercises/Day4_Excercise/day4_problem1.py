# Manipulating data in a dictionary

# Creating a dictionary with initial student information
person = {'name': 'Alice', 'age': 25, 'grade': 'A'}

# Adding a new key-value pair to the dictionary
person['address'] = '123 Main St.'

# Updating an existing value (age)
person['age'] = 35

# Removing a key-value pair safely
# First checking if 'grade' exists in the dictionary
if 'grade' in person:
    del person['grade']

# Printing the final updated dictionary
print(person)