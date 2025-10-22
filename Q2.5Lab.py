def outer():
    name = "Alice"
    def inner():
        print(name)
    inner()
outer()
