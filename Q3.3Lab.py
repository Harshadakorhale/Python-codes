# 3. Write a program demonstrating super() keyword —Create class Animal with method 
# speak(), and class Dog(Animal) that calls super().speak() and then prints "Dog barks".

class Animal:
    def speak(self):
        print("Dog Barks")

class Dog(Animal):
    def speak(self):
        super().speak()

obj = Dog()
obj.speak()
