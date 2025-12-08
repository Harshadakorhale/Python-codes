# 5. Write a class MathOperations with a static method square(num) that returns the 
# square of a given   number. Test it with num = 6.

class MathOperation:
    @staticmethod
    def square(num):
        return num**2
print(MathOperation.square(6))