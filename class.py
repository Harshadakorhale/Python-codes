# class A:
#     def d(self,a,b): 
#         self.a=a
#         self.b=b
#         print(self.a,self.b)
# obj = A()
# obj.d(10,20) #In Fun Definition self keyword is given because at the time of execution A.d(obj,a,b) is passed to the function definition

class A:
    def d(self,a,b): 
       self.a = a
       self.b = b
       return self.a,self.b
obj = A()
print(obj.d(10,20))