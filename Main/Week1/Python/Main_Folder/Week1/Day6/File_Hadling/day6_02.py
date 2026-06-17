#write

with open('sample1.txt', 'w') as file:
    file.write('Hello World')
    file.writelines(['Alice', 'Bob', 'Cherry'])

#File is automatically closed once the program is run
