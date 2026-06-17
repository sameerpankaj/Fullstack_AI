#Word Frequency Counter

# sentence = input('Enter a sentence: ')

# #split the sentence into words
# words = sentence.split()

# #Initialize an empty Dictionary
# word_count = {}

# #count word frequency
# for word in words:
#     word = word.lower()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)

# Taking input sentence from the user
sentence = input('Enter a sentence: ')

# Removing commas so words are not split or counted incorrectly
# This ensures "hello, world" is treated as "hello world"
sentence = sentence.replace(",", " ")

# Splitting the sentence into words based on spaces
words = sentence.split()

# Initializing an empty dictionary to store word frequency
word_count = {}

# Counting frequency of each word
for word in words:
    # Converting word to lowercase to avoid case-sensitive duplicates
    word = word.lower()

    # If word already exists in dictionary, increase its count
    if word in word_count:
        word_count[word] += 1
    else:
        # If word is not in dictionary, add it with count 1
        word_count[word] = 1

# Printing final word frequency dictionary
print(word_count)
