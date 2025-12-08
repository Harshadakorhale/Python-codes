#Class method is belongs to class rather than object 
#cls keyword is used
#class method is used to acced class variable and modify
#Syntax - @classmethod

# class A:
#     a = None
#     @classmethod
#     def prin(cls):
#         print(cls.a)
# A.a=10
# A.prin()

class A:
    @classmethod
    def sum(cls,a,b):
        return a+b
print(A.sum(10,20))
