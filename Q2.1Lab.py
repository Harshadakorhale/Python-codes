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