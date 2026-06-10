'''

Dictionaries in Python

A dictionary in Python is a collection of key–value pairs.
It is used to store data in a structured way, where each value is accessed using a unique key.

🔹 Creating a Dictionary
# Simple dictionary
student = {
    "name": "Sameer",
    "age": 20,
    "course": "Python"
}
🔹 Accessing Values
print(student["name"])   # Sameer
print(student["age"])    # 20
🔹 Adding / Updating Items
student["age"] = 21          # update value
student["city"] = "Frankfurt" # add new key-value pair

print(student)
🔹 Removing Items
student.pop("course")  # removes "course"
# or
del student["age"]     # deletes age key
🔹 Looping Through Dictionary
for key in student:
    print(key, student[key])
🔹 Useful Dictionary Methods
print(student.keys())    # all keys
print(student.values())   # all values
print(student.items())   # all key-value pairs
🔹 Example Program
person = {
    "name": "Alex",
    "age": 25,
    "city": "Berlin"
}

for key, value in person.items():
    print(key, ":", value)
🔥 Key Features of Dictionaries
Data stored as key : value
Keys must be unique
Values can be anything (int, string, list, etc.)
Mutable (can be changed)
📊 Real-Life Example

Think of a dictionary like:

Name → Value
"name" → "Sameer"
"age" → 20

Like a real dictionary:

Word → Meaning
'''