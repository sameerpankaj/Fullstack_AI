import re  # Import the regular expressions module

# Create a string containing a phone number
text = 'Contact me at 123-456-7890'

# Find all groups of one or more digits in the text
# \d matches any digit (0-9)
# + means one or more occurrences
digits = re.findall(r'\d+', text)

# Print the list of digit groups found
print(digits)

# Replace every digit in the text with 'X'
# \d matches each individual digit
#this is used for privacy reasons, to hide your confidential details
udpated_text = re.sub(r'\d', 'X', text)

# Print the modified text
print(udpated_text)


'''

Output:

['123', '456', '7890']
Contact me at XXX-XXX-XXXX


'''