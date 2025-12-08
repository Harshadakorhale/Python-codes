# 5. Write a Python program where a nested function accesses a variable name = "Alice" 
#    from the outer function.

def outer():
    name = "Alice"
    def inner():
        print(name)
    inner()
outer()
