class A:
    def a(self):
        print("Parent class")
class B(A):
    def b(self):
        print("Child class")

obj = B()
obj.a()
obj.b()
