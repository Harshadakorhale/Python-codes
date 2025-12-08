# 6. Write a program to demonstrate containership:Create a class Engine with method 
# start(), and a class Car that contains an object of Engine. Call the start() method 
# through Car. 

class Engine:
    def start(self):
        
        print("Engine started...")
class Car:
    def __init__(self):
     self.engine = Engine()

    def carstart(self):
        self.engine.start()
        print("Car started..")

obj = Car()
obj.carstart()
