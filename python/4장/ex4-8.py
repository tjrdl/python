phone = input("하이픈(-)을 포함한 휴대폰 번호 입력")

for x in phone:
    if x != "-":
        print(x,end="")
