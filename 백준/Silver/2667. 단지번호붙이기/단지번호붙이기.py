import sys

n = int(input())

graph = [sys.stdin.readline().rstrip() for _ in range(n)]

visited = [[0] * n for _ in range(n)]

apt = []

def dfs(x, y):
    visited[x][y] = 1
    cnt = 1
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not visited[nx][ny] and graph[nx][ny] == '1':
            cnt += dfs(nx, ny)
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            apt.append(dfs(i, j))

apt.sort()
print(len(apt))
for elem in apt:
    print(elem)