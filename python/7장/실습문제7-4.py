def Calc(tup):
    sum = 0
    for i in range(len(tup)):
        sum += tup[i]
    return sum




tup1 = (10,20,30,40,50)
result = Calc(tup1)
print("튜플의 합계: ",result)

