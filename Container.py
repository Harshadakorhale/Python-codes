#In container one class use object of another class

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

