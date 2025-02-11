class Calc:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def result(self):
        res = (self.x + self.y) / 2 * self.h
        return res
    
str1 = int(input("사다리꼴 밑변의 길이를 입력하세요: "))
str2 = int(input("윗변의 길이를 입력하세요: "))
str3 = int(input("높이를 입력하세요: "))

done = Calc(str1,str2,str3)
print("사다리꼴의 면적: ",done.result())