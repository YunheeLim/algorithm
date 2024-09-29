import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

# def dfs(x, y, cnt):
#     visited[x][y] = cnt

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
#             dfs(nx, ny, cnt + 1)

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1

    cnt = 1

    while q:
        x, y = q.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = cnt
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

# for i in graph:
#     print(i)

# print()

ans = 0
for i in visited:
   for j in i:
       if j > ans:
           ans = j
print(ans)