class Classroom:
    def detail(self):
        print("This is a classroom")
class College:
    def __init__(self):
     self.classroom = Classroom()

    def info(self):
        self.classroom.detail()
        print("Welcome to Jadhvar college")

obj = College()
obj.info()

