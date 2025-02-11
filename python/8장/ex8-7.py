class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)

# Person class를 상속받은 Student class
class Student(Person):
    pass

x = Student("JJY")
x.show_name()