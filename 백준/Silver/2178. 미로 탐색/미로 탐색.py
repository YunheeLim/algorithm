import sys
from collections import deque

n, m = map(int, input().split())

graph = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

bfs(0, 0)
print(visited[n - 1][m - 1])