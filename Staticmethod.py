#Static method is belongs to class rather than object
#Static method is called 

class A:
    @staticmethod
    def sum(a,b):
        return a+b
print(A.sum(10,20))