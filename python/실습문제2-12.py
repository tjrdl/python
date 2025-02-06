price = int(input("책 값은?"))
dec = int(input("할인율은?"))
ship = int(input("배송료는?"))

result = price - (price*(dec/100)) + ship

print("책 값:",price,"원")
print("할인율:",dec)
print("배송료:",ship,"원")

print("결제 금액: ",int(result),"원")