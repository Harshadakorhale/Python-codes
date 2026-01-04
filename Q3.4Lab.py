# # a = (3+4j)
# # b = (2+5j)
# # print(a+b)
# class Complex_number:
#     a = None
#     b = None
#     def sum(self,c=a+b,x=a+b):
#         return self.c+self.x
    
#     # def sum(self,x):
#     #     return x

# obj = Complex_number()   
# print(obj.sum())
# # obj.sum()
# obj.a=4
# obj.b=5j

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading +
    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)

    # Overloading -
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imag - other.imag)

    # To display object in a + bj format
    def __str__(self):
        return f"{self.real}+{self.imag}j"


# ---- Example Usage ----
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(2, 5)

c3 = c1 + c2       # (3+4j) + (2+5j)
c4 = c1 - c2       # (3+4j) - (2+5j)

print("Addition:", c3)
print("Subtraction:", c4)
