temp = {
    "월": 15.5,
    "화": 17.0,
    "수": 16.2,
    "목": 12.9,
    "금": 11.0,
    "토": 10.5,
    "일": 13.3,
}
min = temp["월"]
for key in temp:
    a = temp[key]
    if a < min:
        min = a
        day = key
print("요일:" ,day,", 최저 기온:",min)

