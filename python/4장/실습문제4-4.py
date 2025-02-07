i = 1
sum = 0

while i <= 100:
    if i % 2 == 1:
        sum += i
        print(sum, end=" ")
        i += 1
    else:
        i += 1
