#Global scope

greeting = 'Hi' #Global variable as it is created outside the function 

def say_hello():#function definition
    print(f' This will print from inside the function: {greeting}')

say_hello() #function call , this will print HI
print(f'This will print from outside the function: {greeting}')#it will print the value passed to varibale greeting as the variable is created globally, this will also print Hi