class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name,"Person class")

    def show_age(self):
        print(self.age)


# Person class를 상속받은 Student class
class Student(Person):
    def show_name(self): # overriding
        print("Student class")
        print(self.name,"Student class")


x = Student("JJY","25")
x.show_name() # 자식의 메소드를 호출하게 됨
x.show_age()
