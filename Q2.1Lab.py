# 1. Write a function outer() that defines a variable message = "Hello" and a nested 
#    function inner() that changes message to "Hi" using nonlocal. Print the value of 
#    message before and after calling inner(). 

def outer():
    message = "Hello"
    print("Before calling inner function : ",message)
    def inner():
        nonlocal message
        msg = "Hi"
        message = msg
    inner()
    print("After calling inner function : ",message)
outer()
