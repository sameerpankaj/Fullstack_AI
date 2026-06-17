#join()

# Creating a string (sentence)
sentence = 'Python is fun'

# Splitting the sentence into a list of words
# By default, split() separates words based on spaces
words = sentence.split()

# Printing the list of words
print(words)

# Joining the list of words back into a single string
# ' ' (space) is used as a separator between words
new_sentence = ' '.join(words)

# Printing the reconstructed sentence
print(new_sentence)