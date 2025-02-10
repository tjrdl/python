def func(n):
    list1 = []
    for i in range(n):
        if i == 0:
            continue
        list1.append(i * i)
    return list1


str = int(input("n 값을 입력하세요: "))
result = func(str)
print(result)
