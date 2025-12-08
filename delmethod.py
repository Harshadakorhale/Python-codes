# class A:
#     def __del__(self,a,b): #without constructor 
#         self.a = a
#         self.b = b
#         print(self.a,self.b)
    
# obj = A(5,6)
# print("Object is distroyed:")

class A:
    def __del__(self):
        print("object is distroyed")