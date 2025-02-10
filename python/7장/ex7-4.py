# 매개변수를 리스트로 받아 처리 가능능
def func(food):
    # for x in food:
    #     print(x)
    food.append("strawberry")


# func(["apple","orange","banana"])
fruit = ["apple", "orange", "banana"]
print(fruit)
func(fruit)
print(fruit)
