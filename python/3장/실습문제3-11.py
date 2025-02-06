number1 = int(input("첫 번째 숫자를 입력하세요: "))
number2 = int(input("두 번째 숫자를 입력하세요: "))
sum = number1 + number2
print(number1, "+", number2, "=", sum)

if sum % 3 == 0:
    print(sum, "은(는) 3의 배수가 맞다.")
else:
    print(sum, "은(는) 3의 배수가 아니다.")
