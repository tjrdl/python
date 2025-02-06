year = input("년도?")
month = input("월은?")
day = input("일은?")

result = "{0}.{1}.{2}".format(year, month, day)
print(result)


print("sep(): " + year, month, day, sep=".")
