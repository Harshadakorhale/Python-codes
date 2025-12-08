class A:
    def methoda(self):
        print("Class A calling")
class B:
    def methodb(self):
        print("Class B Calling")
class C(A,B):
    def methodc(self):
        print("Class C is calling")

obj = C()
obj.methoda()
obj.methodb()
obj.methodc()