import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque([(x, y)])
    union = [(x, y)]
    visited[x][y] = True
    total = arr[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    visited[nx][ny] = True
                    total += arr[nx][ny]
                    cnt += 1
                    union.append((nx, ny))
                    q.append((nx, ny))

    new_population = total // cnt
    for ux, uy in union:
        arr[ux][uy] = new_population
    return len(union) > 1

ans = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    moved = True

    if not moved:
        break
    ans += 1

print(ans)