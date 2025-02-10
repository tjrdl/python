numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
i = 0
sum = 0
list1 = []

result = []
result += numbers[1::2]
while i < len(numbers):
    if i % 2 == 1:
        sum += numbers[i]
        list1.append(numbers[i])
    i += 1
print("짝수 번째 요소: ",list1)
print(sum)
print(result)
