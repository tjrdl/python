s = "Python is sidely used by a number of big companies".lower()
i = 0
count = 0

print("모음: ", end=" ")

while i <= len(s) - 1:
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        count += 1
        print(s[i], end=" ")
    i += 1
print()
print("모음 개수 %d" % count)
