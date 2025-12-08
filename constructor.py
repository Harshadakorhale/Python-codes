# Constructor is a special method it is called automatically when object is created
#syntax : def __init__():
# class A:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def display(self):
#        print(self.a,self.b)
    
# obj = A(5,6)
# obj.display()

class A:
    def a(self,a,b): #without constructor 
        self.a = a
        self.b = b

    def display(self):
       print(self.a,self.b)
obj = A()
obj.a(5,6)
obj.display()
