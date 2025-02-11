class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# Person class를 상속받은 Student class
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    pass


x = Student("JJY","25")
x.show_name()
x.show_age()
