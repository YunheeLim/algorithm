from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_len = 0

def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0

def bfs(sx, sy):
    global max_len

    q = deque([(sx, sy)])
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]):
                visited[nx][ny] = visited[x][y] + 1

                if (visited[nx][ny] >= max_len):
                    max_len = visited[nx][ny]
                    pw = arr[sx][sy] + arr[nx][ny]
                    ans.append((max_len, pw))

                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if(arr[i][j]):
            bfs(i, j)
            clear_visited()

ans.sort(key=lambda x:(-x[0], -x[1]))

print(ans[0][1])


                
