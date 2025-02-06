month = int(input("월을 숫자로 입력하세요: "))

if 3 <= month <= 5:
    print(month, "월은 봄입니다.")
elif 6 <= month <= 8:
    print(month, "월은 여름입니다.")
elif 9 <= month <= 11:
    print(month, "월은 가을입니다.")
elif 1 <= month <= 2 or month == 12:
    print(month, "월은 겨울입니다.")
else:
    print("1~12 사이 숫자로 입력")
