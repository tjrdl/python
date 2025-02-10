def reverse(char):
    i = len(char) - 1
    while i >= 0:
        print(char[i],end="")
        i-=1



str = input("문자열을 입력하세요: ")
reverse(str)