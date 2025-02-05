price = 3000
num = 3
pay = 10000

change = pay - price * num

# print(change)

# 오류발생
# print("거스름돈--->원" change)

# 오류
# print("거스름돈 ---> 원" % change)

# change 변수를 %d(정수)로 받음
print("거스름돈 ---> %d원" % change)

# change 변수를 %f(실수)로 받음
print("거스름돈 ---> %.2f원" % change)
