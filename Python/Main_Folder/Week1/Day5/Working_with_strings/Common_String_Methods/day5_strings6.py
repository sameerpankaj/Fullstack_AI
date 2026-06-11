#replace()


# Creating a string (sentence)
sentence = 'Python is fun'

# Splitting the sentence into a list of words
# By default, split() separates words based on spaces
words = sentence.split()

# Joining the list of words back into a single string
# ' ' (space) is used as a separator between words
new_sentence = ' '.join(words)

# Creating a new string
text = 'I love Java'

# Replacing a word in the string
# NOTE: 'Javaa' is a typo, so replacement will not work as expected
updated_text = text.replace('Java', 'Python')

# Printing the updated string

print(updated_text)