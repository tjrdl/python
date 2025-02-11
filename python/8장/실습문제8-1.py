class Ract:
    def __init__(self,r,h):
        self.r = r
        self.h = h
    def calc(self):
        result = (int(self.r) * int(self.h)) / 2
        print("삼각형의 면적: ",result)
    
str1 = input("삼각형 밑변의 길이를 입력하세요: ")
str2 = input("높이를 입력하세요: ")

Ractangle = Ract(str1,str2)
Ractangle.calc()