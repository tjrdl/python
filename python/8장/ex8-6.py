class Members:
    total = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Members.total += 1

    def show_info(self):
        print("name: %s\n phone:%s" % (self.name, self.phone))


m1 = Members("JJY1", "01012345678-1")
m2 = Members("JJY2", "01012345678-2")
m3 = Members("JJY3", "01012345678-3")
m1.show_info()
m2.show_info()
m3.show_info()

print("total member:", Members.total)

