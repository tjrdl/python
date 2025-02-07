count = 0

for a in range(200, 801):
    if a % 5 != 0:
        print(a, end=" ")
        count += 1
    if count % 10 == 0:
        print()
    a += 1
