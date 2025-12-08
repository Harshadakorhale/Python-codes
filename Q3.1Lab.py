# 1. Create a class Student with attributes name, roll_no, and marks. Define a method 
# display() to print details. Create two student objects and display their info.

class Student:
    name1 = None
    rollno = None
    marks = None
    def __init__(self,name1,rollno,marks):
        self.name = name1
        self.rollno = rollno
        self.marks = marks
    
    def display(self):
        print(f"name of student is: {self.name}")
        print(f"roll no is:{self.rollno}")
        print(f"marks are: {self.marks}")

obj1 = Student("Harshada",101,90)
obj2 = Student("Shweta",102,92)

obj1.display()
obj2.display()