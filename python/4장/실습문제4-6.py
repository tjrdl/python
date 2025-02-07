i = 1
count = 0
while i <= 1000:
    if i % 3 == 0:
        i += 1
    else:
        print(i,end=" ")
        i += 1
        count += 1
    if count % 10 == 0:
        print()