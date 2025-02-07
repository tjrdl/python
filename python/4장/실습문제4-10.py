str = input("숫자를 입력하세요")
res = int(str)
len = len(str)
count = 0
for i in range(len):
    print(str[i])
    if int(str[i]) % 2 == 1:
        count += 1
    i += 1
print("홀수의 개수: ", count, "개")

