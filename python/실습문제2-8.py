o_length = int(input("윗변의 길이는?"))
u_length = int(input("밑변의 길이는?"))
height = int(input("높이는?"))

res = (o_length + u_length) * height / 2

result = "{:.1f}".format(res)

print("-사다리꼴의 면적:", result)
