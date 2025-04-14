n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt, sum):
    global answer
    if cnt == 3:
        answer = max(answer, sum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, sum + arr[nx][ny])
            visited[nx][ny] = False # 백트래킹

def T_shape(x, y):
    global answer
    sum = arr[x][y]
    len = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            sum += arr[nx][ny]
            len += 1
    if len == 5:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            answer = max(answer, sum - arr[nx][ny])
    elif len == 4:
        answer = max(answer, sum)

answer = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = True # 여기서 visited를 새로 생성하면 4중 for문으로 시간초과 뜨니까 백트래킹 처리하기!!!
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = False
        T_shape(i, j)

print(answer)