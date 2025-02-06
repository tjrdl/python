num1 = int(input("첫 번째 숫자를 입력하세요"))
num2 = int(input("두 번째 숫자를 입력하세요"))

str = input("원하는 연산 입력: ")

if str == "+" :
    print(num1,"+",num2,"=",num1+num2)
elif str == "-" :
    print(num1,"-",num2,"=",num1-num2)
elif str == "*" :
    print(num1,"*",num2,"=",num1*num2)
elif str == "/" :
    print(num1,"/",num2,"=%.2f"%(num1/num2))
else :
    print("선택 오류!")



