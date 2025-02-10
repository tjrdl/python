def average(*args):
    print(args)  # 출력이 튜플형식
    num_args = len(args)
    sum = 0
    for i in range(num_args):
        sum += args[i]
    avg = sum / num_args
    return avg


print("%.1f" % average(85, 96, 87))
