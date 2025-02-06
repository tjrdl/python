num = input("숫자를 입력하세요: ")
a = num[-3::3]

if int(a) % 2 == 0:
    print(a, "은(는) 짝수이다.")
else:
    print(a, "은(는) 홀수이다.")
