'''
Check if a String is a Palindrome
--  Palindrome is a word or phrase or sequence that reads the same backward as well as forward
for example 'Madam', it reads same from left or right

also example: A man, A plan, A canal, Panama

'''

def is_palindrome(text):
    text = ''.join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input('Enter a string or text: ')
if is_palindrome(input_text):
    print(f'the {input_text} is a palindrome')
else:
    print(f'The {input_text} is not a palindrome')
