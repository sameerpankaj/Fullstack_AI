#Local Scope
def greet(): #function defintion
    message = 'Hello World' #Local variable
    print(message)

greet()#Function call : here it will print Hello World
#print(message)#This will throw an error as this is outside the function and the varibale message is created inside the function, that is local variable