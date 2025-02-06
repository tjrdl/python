score1 = int(input("필기시험 점수는?"))
score2 = int(input("실기시험 점수는?"))

print("-필기시험 점수: ", score1)
print("-실기시험 점수: ", score2)


if score1 >= 80 and score2 >= 80:
    print("-판정: 합격")
else:
    print("-판정: 불합격")
