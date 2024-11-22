n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]

# 초기 구름 위치 설정
clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]

# 이동 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물복사 대각선 방향
diag_dx = [-1, -1, 1, 1]
diag_dy = [-1, 1, -1, 1]

# 물복사 버그 해결
def copy(x, y):
    for i in range(4):  # 대각선 방향
        nx, ny = x + diag_dx[i], y + diag_dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
            arr[x][y] += 1

# 새로운 구름 생성
def newCloud(visited):
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not visited[i][j]:
                new_clouds.append((i, j))
                arr[i][j] -= 2
    return new_clouds

# 구름 이동
for move in moves:
    d, s = move
    d -= 1  # 방향 조정
    visited = [[False] * n for _ in range(n)]

    # 구름 이동 및 물 증가
    for i in range(len(clouds)):
        x, y = clouds[i]
        nx = (x + dx[d] * s) % n  # 경계 처리
        ny = (y + dy[d] * s) % n
        clouds[i] = (nx, ny)  # 갱신
        arr[nx][ny] += 1
        visited[nx][ny] = True

    # 물복사
    for x, y in clouds:
        copy(x, y)

    # 새 구름 생성
    clouds = newCloud(visited)

# 결과 계산
ans = sum(sum(row) for row in arr)
print(ans)
