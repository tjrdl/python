def func1(km):
    mile = km * 0.621371
    return mile

km = int(input("킬로미터를 입력하세요: "))
print(km,"킬로미터는 ",func1(km),"마일이다.")
