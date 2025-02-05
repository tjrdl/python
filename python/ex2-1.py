# input("enter your name: ")
name = input("enter your name: ")
birth = input("당신이 태어난 해는?: ") # 숫자를 입력해도 문자로 받음
birth2 = int(input("your birth?: ")) # 입력받은 문자열을 정수로 바꿈꿈

# int - str 오류
# age = 2025 - birth 

# int형 변환
age = 2025 - int(birth)

# int - int 에러 없음
age2 = 2025 - birth2

# %s : 문자열을 받음
print("%s님이 태어난 해는 %s" % (name,birth))

# not str 오류
# print("%d님" % name)

# not str 오류
# print("%s님이 태어난 해는 %d" % (name,birth))

print("%s님의 나이는 %d살 입니다." % (name,age))
