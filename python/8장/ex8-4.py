class Members:
    def __init__(self, name, age):
        # pass # 동작 없이 다음 실행
        self.name = name
        self.age = age

    def get_info(self):
        print("get value", self.name)
        print("get value", self.age)


member = Members("jjy", "25")
member.get_info()
