str = input("문장을 입력해 주세요: ")
i = len(str)

while i > 0:
    result = str[i - 1]
    print(result.replace(" ", "-"), end="")
    i -= 1
