num1 = int(input("시작수는?"))
num2 = int(input("끝수는?"))
num3 = int(input("정수를 입력하세요: ?"))

if num1 <= num3 <= num2:
    print(num3, "은(는)", num1, "~", num2, "사이에 있다.")
else:
    print(num3, "은(는)", num1, "~", num2, "사이에 없다.")
