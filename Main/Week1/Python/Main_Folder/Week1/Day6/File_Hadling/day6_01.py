#with statement

with open('sample.txt', 'w') as file: # this only creates file in write or append mode
    content = file.read()
    print(content)