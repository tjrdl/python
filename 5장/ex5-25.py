phone1_list1 = ["010-1234-5678","010-2345-5678","010-1111-2222"]
print(phone1_list1)

phone2_list2 = []

for number in phone1_list1:
    x = number.replace("-","")
    phone2_list2.append(x)
print(phone2_list2)