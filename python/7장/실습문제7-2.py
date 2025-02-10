def add():
    return x + y


def sub():
    return x - y


def mul():
    return x * y


def div():
    return x / y


a = int(input("1 더하기 \n 2. 빼기 \n 3. 곱하기 \n 4.나누기 \n 원하는 연산을 선택"))
x = int(input("첫 번째 숫자를 입력하세요: "))
y = int(input("두 번째 숫자를 입력하세요: "))

if a == 1:
    print(add())
elif a == 2:
    print(sub())
elif a == 3:
    print(mul())
elif a == 4:
    print(div())
