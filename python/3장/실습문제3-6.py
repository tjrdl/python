str = input("영문 소문자 하나를 입력하세요: ").lower()

if str == "a" or str == "e" or str == "i" or str == "o" or str == "u":
    print(str, "은(는) 모음이다.")
else:
    print(str, "은(는) 자음이다.")

a = ["a", "e", "i", "o", "u"]
length = len(a)

if str in a:
    print(str, "은(는) 모음이다.")
else:
    print(str, "은(는) 자음이다.")
