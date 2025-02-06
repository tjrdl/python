age = int(input("나이는?"))
ticket = 2000
print("나이:", age, "세")

if age < 65:
    print("입장료: %d원" % ticket)
else:
    ticket = 0
    print("입장료: %d원" % ticket)
