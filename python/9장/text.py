def dfs(num, min_x, max_x, min_y, max_y, min_area):
    if num == k + 1:
        return min(min_area, (max_x - min_x) * (max_y - min_y))

    for x, y in colors[num]:
        x1, x2 = min(min_x, x), max(max_x, x)
        y1, y2 = min(min_y, y), max(max_y, y)
        if min_area > (x2 - x1) * (y2 - y1):
            min_area = dfs(num + 1, x1, x2, y1, y2, min_area)
    
    return min_area


# 입력 받기
n, k = map(int, input().split())  # 점 개수 n, 색깔 개수 k
colors = [[] for _ in range(k + 1)]

for _ in range(n):
    x, y, color_index = map(int, input().split())  # k 대신 color_index 사용
    colors[color_index].append((x, y))  # 좌표 저장

# 초기 값 설정
INF = float('inf')
min_area = dfs(1, INF, -INF, INF, -INF, 2000 * 2000)

# 최소 영역 출력
print(min_area)
