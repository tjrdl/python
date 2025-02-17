# 두 개의 값을 split을 사용하여 한번에 받아옴
N, K = map(int, input().split())
colors = [[] for i in range(K + 1)]
if 1 <= N <= 100 and 1 <= K <= 20:
    for i in range(N):
        x, y, k = map(int, input().split())
        if -1000 <= x <= 1000 and -1000 <= y <= 1000 and 1 <= k <= K:
            colors[k].append((x, y))
        else:
            print("wrong number")

str = colors[1][0]
for x in colors:
    print('x={0}'.format(x))