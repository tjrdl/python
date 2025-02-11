class Cat:
    kor_name = "rocky_korea"
    end_name = "rockyeng"
    eng_name = "rocky"
    age = 2

    def sound(self):
        print("meow")

    def speed(self):
        print("faster")


mycat = Cat()
print(mycat.kor_name)
print(mycat.end_name)
print(mycat.eng_name)
print(mycat.age)
mycat.sound()
mycat.speed()
