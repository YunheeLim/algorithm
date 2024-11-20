n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_sum = 0

def dfs(x, y, cnt, sum):
    global max_sum
    if cnt == 4:
        max_sum = max(sum, max_sum)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, sum + arr[nx][ny])
            visited[nx][ny] = 0

def check_special_shape(x, y):
    global max_sum
    for shape in [[(0, 1), (0, -1), (-1, 0)],  # ㅗ
                  [(0, 1), (0, -1), (1, 0)],   # ㅜ
                  [(1, 0), (-1, 0), (0, 1)],   # ㅏ
                  [(1, 0), (-1, 0), (0, -1)]]: # ㅓ
        total = arr[x][y]
        valid = True
        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                total += arr[nx][ny]
            else:
                valid = False
                break
        if valid:
            max_sum = max(max_sum, total)

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0
        check_special_shape(i, j)

print(max_sum)