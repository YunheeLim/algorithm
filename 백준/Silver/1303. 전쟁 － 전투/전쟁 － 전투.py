from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]

visited = [[False] * n for _ in range(m)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def bfs(i, j, color):

    cnt = 0
    queue = deque()

    if graph[i][j] == color and not visited[i][j]:
        queue.append((i, j))
        visited[i][j] = True
        cnt += 1


    while queue:
        x, y = queue.popleft()
        for dir in range(len(dxs)):
            nx = x + dxs[dir]
            ny = y + dys[dir]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt*cnt

w, b = 0, 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            w += bfs(i, j, graph[i][j])
        elif graph[i][j] == 'B':
            b += bfs(i, j, graph[i][j])

print(w, b)
