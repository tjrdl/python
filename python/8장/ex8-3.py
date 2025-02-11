class Members:
    name = "name1"

    def set_info(self, name):
        self.name = name  # 객체의 속성이다
        print(name)

    def get_info(self):
        print("get value", self.name)


member = Members()

member.set_info("jjy")
member.get_info()

member.set_info("jjy2")
member.get_info()
