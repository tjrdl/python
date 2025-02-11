class Student:
    def __init__(self):
        self.pet = []

    def push_pet(self, x):
        self.pet.append(x)


john = Student()
john.push_pet("cat")
print(john.pet)

sally = Student()
sally.push_pet("iguana")

print(sally.pet)
