id = input("아이디는?")
level = 0
if id == "admin":
    print("콘텐츠 이용이 가능합니다!")
else:
    level = int(input("회원 레벨은?(1~9)"))
    if 1 <= level <= 3:
        print("콘텐츠를 이용할 수 있습니다!")
    else:
        print("콘텐츠를 이용할 수 없습니다!")
