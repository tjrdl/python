print("-" * 30)
print("섭씨 화씨")
print("-" * 30)

for c in range(-20, 1, 5):
    f = c * 9.0 / 5.0 + 32.0
    print("{0:5},{1:5.1f}".format(c, f))

print("-" * 30)
