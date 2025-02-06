num = int(input("양의 정수를 입력하세요: "))

if num % 3 == 0:
    if num % 4 == 0:
        print(num,"은(는) 3과 4의 배수이다.")
    else :
        print(num,"은(는) 3의 배수이다.")
elif num % 4 == 0:
    if num % 4 == 0:
        print(num,"은(는) 3과 4의 배수이다.")
    else :
        print(num,"은(는) 4의 배수이다.")
else :
    print(num,"은(는) 3도 4의 배수도아니다.")


