numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
sum = 0
i = 0
len = len(numbers)
while len > 0:
    sum += numbers[i]
    i += 1
    len -= 1
print(sum)
