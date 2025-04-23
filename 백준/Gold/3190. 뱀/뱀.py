import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1
l = int(input())
directions = {}
for _ in range(l):
    x, c = input().split()
    directions[int(x)] = c
visited = [[False] * n for _ in range(n)]

# 오 아래 왼 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
snake = deque([(0, 0)])
arr[0][0] = 2 # 뱀
dir = 0
cnt = 0
x, y  = 0, 0
while True:
    cnt += 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
        snake.append((nx, ny))
        if arr[nx][ny] != 1: # 사과 없음
            sx, sy = snake.popleft() # 길이 유지
            arr[sx][sy] = 0
        arr[nx][ny] = 2
        x, y = nx, ny
        if cnt in directions:
            if directions[cnt] == 'D':
                dir = (dir + 1) % 4
            else:
                dir = (dir + 3) % 4
    else:
        break
    # for e in arr:
    #     print(e)
    # print()
print(cnt)