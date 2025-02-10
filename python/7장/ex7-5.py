def func(n):
    x = n + 5  # 지역
    global b  # 전역
    return x


x = 200  # 전역
a = func(10)
print(x)
print(a)
print(x)
