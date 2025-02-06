print("기능 선택 \n 1. 더하기 \n 2. 빼기 \n 3. 곱하기 \n 4. 나누기")

str = input("계산기 기능을 선탁해사에(1/2/3/4): ")


num1 = int(input("첫 번째 숫자를 입력하세요"))
num2 = int(input("두 번째 숫자를 입력하세요"))


if str == "1" :
    print(num1,"+",num2,"=",num1+num2)
elif str == "2" :
    print(num1,"-",num2,"=",num1-num2)
elif str == "3" :
    print(num1,"*",num2,"=",num1*num2)
elif str == "4" :
    print(num1,"/",num2,"=%.2f"%(num1/num2))
else :
    print("선택 오류!")



