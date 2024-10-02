import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs(r, c):
    q = deque([(r, c)])

    distance = r + c

    while q:
        r, c = q.popleft()

        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and (not visited[nx][ny] or visited[nx][ny] > visited[r][c]+1):
                    visited[nx][ny] = visited[r][c] + 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

ans = -1

for i in range(n):
    for j in range(m):
        if ans < visited[i][j]:
            ans = visited[i][j]
print(ans)