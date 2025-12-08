# 12. Create a package calculator with module operations.py containing add(), subtract(), 
# and divide() functions. Import the package and perform operations with values a = 
# 20, b = 4. Then, write another program that imports this module and uses all the functions. 


#use files namely main.py and use_module.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return " Cant Divide by zero!"
    return a / b
