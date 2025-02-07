for a in range(5):
    for b in range(10):
        print("*", end="")
    print()

print()

# for a in range(1,10,2): 
#     i = 10 - a
#     print(" " * i, end="")
#     for b in range(a):
#         print("*", end="")
#     for b in range(a):
#         print("*", end="")
#     print(" " * i, end="") 
    
#     print()

for a in range(10):
    i = 10 - a - 5
    j = -10 + a + 5
    print(" "*i,end="")
    print(" "*j,end="")
    for b in range(a):
        print("*", end="")
    
    print()
