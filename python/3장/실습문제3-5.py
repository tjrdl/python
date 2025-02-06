num1 = int(input("첫 번째 정수는?"))
num2 = int(input("두 번째 정수는?"))
num3 = int(input("세 번째 정수는?"))

if num1 > num2 and num1 > num3:
    print(num1, num2, num3, "중에서 가장 큰 수는 ", num1, "입니다.")
elif num2 > num1 and num2 > num3:
    print(num1, num2, num3, "중에서 가장 큰 수는 ", num2, "입니다.")
elif num3 > num1 and num3 > num2:
    print(num1, num2, num3, "중에서 가장 큰 수는 ", num3, "입니다.")


a = [num1, num2, num3]
print(max(a))
