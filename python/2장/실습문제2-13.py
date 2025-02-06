str = input("하이픈(-)이 포함된 11자리의 휴대폰 번호는?")

result = str.replace("-", "")

print(str)

print("- 하이픈 삭제된 휴대폰 번호: ", result)  
