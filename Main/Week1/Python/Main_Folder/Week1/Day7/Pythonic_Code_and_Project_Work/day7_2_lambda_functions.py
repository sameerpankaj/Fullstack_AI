#Lambda functions

#Create a list of squares
squares = [x**2 for x in range(10)]
# print(squares)

#Filter Even numbers
evens = [x for x in range(100) if x % 2 == 0]
# print(evens)

#lambda arguments: expression
# def function_naem(args){
#     args: 
# }

add = lambda x, y: x + y
print(add(3,5))