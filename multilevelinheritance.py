class A:#parent/super class
    def methoda(self):
        print("Print class A")
class B(A):#child/sub class
    def methodb(self):
        print("Print class B")
class C(B):
    def methodc(self):
        print("Print class c")

obj = C()
obj.methoda()
obj.methodb()
obj.methodc()
