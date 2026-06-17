'''

Create a text cleaner
 -- Write a program that removes unwanted characters
'''

# import re

# def clean_text(text):
#     #Remove Punctuation
#     text = re.sub(r'[^\W\S]', '', text)
#     #Remove extra spaces
#     text = ' '.join(text.split())
#     #Convert to lowercase
#     return text.lower()

# input_text = '  Hello, World.!!! Welcome to Python, Programming...'
# cleaned_text = clean_text(input_text)
# print(f'Cleaned text is {cleaned_text}')


import re  # Import the regular expressions module

# Function to clean the input text
def clean_text(text):
    
    # Remove punctuation and special characters
    # [^\w\s] matches any character that is NOT
    # a letter, digit, underscore, or whitespace
    text = re.sub(r'[^\w\s]', '', text)

    # Remove extra spaces from the text
    # split() separates the text into words
    # join() combines them with a single space
    text = ' '.join(text.split())

    # Convert the text to lowercase and return it
    return text.lower()

# Input string containing extra spaces and punctuation
input_text = '  Hello, World.!!! Welcome to Python, Programming...'

# Call the function to clean the text
cleaned_text = clean_text(input_text)

# Display the cleaned text
print(f'Cleaned text is {cleaned_text}')