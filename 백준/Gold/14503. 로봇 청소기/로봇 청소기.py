n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def canGo(x, y):
    if 0 <= x < n and 0 <= y < m and not arr[x][y] and not visited[x][y]:
        return True
    return False

def dfs(x, y, d):
    global ans
    if not visited[x][y]:
        visited[x][y] = True
        ans += 1

    for _ in range(4):
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        # 청소 가능
        if canGo(nx, ny):
            dfs(nx, ny, d)
            return

    # 청소 불가 = 후진
    nx = x - dx[d]
    ny = y - dy[d]
    if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
        dfs(nx, ny, d)

dfs(r, c, d)
print(ans)