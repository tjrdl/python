# dictionary
member = {"name": "황예린", "age": 22, "email": "yerin@hanmail.net"}
print(member)

score = dict([("국어", 80), ("영어", 90), ("수학", 70)])

# 리스트, 튜블을 사용해서 dictionary를 생성
print(score)

# 키를 사용해 값을 출력
print(score["국어"])
print(score["수학"])
print(score["영어"])

score["음악"] = 90  # 없는 키는 추가
score["수학"] = 77  # 있는 키는 값을 변경경
