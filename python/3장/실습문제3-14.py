num = input("수를 입력하세요: ")
a = len(num)
if a == 1:
    print(num,"은(는) 한 자리 숫자이다.")
elif a == 2:
    print(num,"은(는) 두 자리 숫자이다.")
elif a == 3:
    print(num,"은(는) 세 자리 숫자이다.")
else :
    print("0~999까지의 숫자 입력")

