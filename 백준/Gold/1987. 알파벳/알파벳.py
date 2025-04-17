import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

answer = 0

dx = [ -1, 1, 0, 0]
dy = [0, 0, -1, 1]

history = set()

def dfs(x, y):
    global answer
    answer = max(answer, len(history))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] not in history:
                history.add(arr[nx][ny])
                dfs(nx, ny)
                history.remove(arr[nx][ny])

history.add(arr[0][0])
dfs(0, 0)

print(answer)