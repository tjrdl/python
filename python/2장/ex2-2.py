# 주석 기능
"""작은 따옴표 세개"""
"""큰 따옴표 세개"""


name = input("enter your name: ")
birth = int(input("당신이 태어난 해는?: "))  # 숫자를 입력해도 문자로 받음

age = 2025 - birth
print("%s님의 나이는 %s세 입니다." % (name, age))
