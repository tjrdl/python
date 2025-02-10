a = "I am a genius!"

b = []

c = len(a) - 1


i = 0
while c >= 0 :
    b.append(a[i])
    i += 1
    c -= 1
print(b)