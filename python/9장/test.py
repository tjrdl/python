def dfs(num, min_x, max_x, min_y, max_y, min_area):
    if num == k + 1:
        return min(min_area, (max_x - min_x) * (max_y - min_y))

    for x, y in colors[num]:  # 현재 색깔(num)의 모든 점 탐색
        x1, x2 = min(min_x, x), max(max_x, x)
        y1, y2 = min(min_y, y), max(max_y, y)

        if min_area > (x2 - x1) * (y2 - y1):  
            min_area = dfs(num + 1, x1, x2, y1, y2, min_area)  # 다음 색깔(num+1) 탐색
    
    return min_area


# 입력 받기
n, k = map(int, input().split())  # 점 개수 n, 색깔 개수 k
colors = [[] for _ in range(k + 1)]

for _ in range(n):
    x, y, color_index = map(int, input().split())  # 점의 좌표 및 색깔 정보

    # 📌 제약 조건 추가: 범위를 벗어나면 무시
    if not (-1000 <= x <= 1000 and -1000 <= y <= 1000):
        continue

    colors[color_index].append((x, y))  # 좌표 저장

# 초기 DFS 호출값을 유효한 범위로 설정
min_x, max_x, min_y, max_y = 1000, -1000, 1000, -1000
min_area = dfs(1, min_x, max_x, min_y, max_y, 2000 * 2000)

# 최소 영역 출력
print(min_area)
