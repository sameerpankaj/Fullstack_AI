'''
String Manipulation
    Concatenation
    Slicing
    Formatting

Common String Methods
    split()
    join()
    replace()
    strip()

Regular expression for pattern matching
    What are regular expressions?
    --using the re Module
    Common Functions    
    --re.search(patter, string)
    --re.find(pattern, string)
    --re.sub(pattern, repleacement, string)








'''


'''
A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

Strings are used to store and manipulate text.

🔹 Creating Strings
# Using single quotes
name = 'Alice'

# Using double quotes
city = "Berlin"

# Using triple quotes (for multiple lines)
message = """Hello
Welcome to Python"""
🔹 Accessing Characters
text = "Python"

print(text[0])   # P
print(text[2])   # t
print(text[-1])  # n (last character)
🔹 String Slicing
text = "Python"

print(text[0:3])  # Pyt
print(text[2:5])  # tho
print(text[:4])   # Pyth
print(text[3:])   # hon
🔹 String Length
text = "Python"

print(len(text))  # 6
🔹 String Concatenation
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

print(full_name)

Output:

John Doe
🔹 Repeating Strings
print("Hi! " * 3)

Output:

Hi! Hi! Hi!
🔹 Common String Methods
text = "Hello World"

print(text.lower())      # hello world
print(text.upper())      # HELLO WORLD
print(text.title())      # Hello World
print(text.replace("World", "Python"))
print(text.strip())      # Removes leading/trailing spaces
🔹 Checking Strings
text = "Python"

print(text.startswith("Py"))  # True
print(text.endswith("on"))    # True
print("th" in text)           # True
🔹 Splitting a String
sentence = "Python is easy to learn"

words = sentence.split()

print(words)

Output:

['Python', 'is', 'easy', 'to', 'learn']
🔹 f-Strings (Recommended)
name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")

Output:

My name is Alice and I am 25 years old.
🔥 Important String Properties
Strings are immutable (cannot be changed directly).
Indexing starts at 0.
Strings support slicing.
Many built-in methods are available for text manipulation.
Example:
text = "Python"

# text[0] = "J"  ❌ Error

You cannot modify a character directly because strings are immutable.

Practice Program
# Taking input from the user
name = input("Enter your name: ")

# Displaying information about the string
print("Name:", name)
print("Length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
'''