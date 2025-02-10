def Alpha():
    count = 0
    for i in range(len(str)):
        if(str[i] == idx):
            count += 1
    return count

str = input("영어 문장을 입력하세요: ")
idx = input("알파벳 하나를 입력하세요: ")
print(str,"에 포함된",idx,"의 개수는",Alpha(),"개이다.")