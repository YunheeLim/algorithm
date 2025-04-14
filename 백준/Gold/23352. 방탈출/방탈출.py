from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_len = 0
candidate = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_short_route(x, y):
    global max_len
    sx, sy = x, y
    len_arr = [[int(1e9)] * m for _ in range(n)]
    q = deque([(x, y)])
    len_arr[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and len_arr[nx][ny] > len_arr[x][y] + 1:
                len_arr[nx][ny] = len_arr[x][y] + 1
                q.append((nx, ny))

    if len_arr[x][y] >= max_len:
        max_len = len_arr[x][y]
        candidate.append((max_len, arr[sx][sy] + arr[x][y]))

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            find_short_route(i, j)
candidate.sort(key=lambda x: (-x[0], -x[1]))
print(candidate[0][1])