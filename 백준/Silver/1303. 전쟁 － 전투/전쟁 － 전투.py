import sys
sys.setrecursionlimit(3000000)

n, m = map(int, input().split())

board = [list(input()) for _ in range(m)]

def dfs(x, y, cnt):
    color = board[x][y]
    board[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == color:
            cnt = dfs(nx, ny, cnt + 1)
 
    return cnt
    
cntW, cntB = 0, 0

for i in range(m):
    for j in range(n):
        if board[i][j] == 'W':
            cntW += (dfs(i, j, 1))**2
        elif board[i][j] == 'B':
            cntB += (dfs(i, j, 1))**2

print(cntW, cntB)