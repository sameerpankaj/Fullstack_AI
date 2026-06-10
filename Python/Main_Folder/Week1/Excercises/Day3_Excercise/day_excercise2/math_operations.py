#Build a custom python module

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Division by zero is not allowed'