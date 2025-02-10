car = {"brand": "현대", "model": "아반떼", "start": 1990, "year": 2021}
print(car)

x = car.pop("start")  # 키에 해당하는 값 잘라내기기
print(x)

print(car)

# 키와 값을 모두 삭제제
car.clear()
print(car)
