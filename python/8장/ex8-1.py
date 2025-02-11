class Person:
    # name: 속성성
    name = "김정연"

    # person1 객체를 self가 받음음
    def hi(self):  # hello 메소드 호출될때 객체를 self 받음음
        # print("hello")
        print(Person.name + "님 안녕하세요")


person1 = Person()  # 객체 생성

person1.hi()  # method 호출출

Person.name = "황서영"
person1.hi()
