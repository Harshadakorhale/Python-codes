class A:
    def methoda(self):
        print("A calling")
class B(A):
    def methodb(self):
        print("B calling")
class C(A):
    def methodc(self):
        print("C calling")

obj = C()
obj.methoda()
obj.methodc()
obj1 = B()
obj1.methodb()