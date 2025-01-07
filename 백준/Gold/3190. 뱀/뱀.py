from collections import deque

n = int(input())
k = int(input())
apples = []
changes = []
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 1
time = 0

arr = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    apples.append((r, c))

l = int(input())

for _ in range(l):
    x, c = input().split()
    changes.append((int(x), c))

visited[0][0] = True
x, y = 0, 0

# 경로 히스토리
path = []
path.append((x, y))

def bfs(sx, sy):
    global time, dir, path
    q = deque([])
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        # print('next:', nx, ny)
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # print('time:', time)
            time += 1
            # 방향 바꿀 때
            for change in changes:
                if change[0] == time:
                    if change[1] == 'L': # 왼쪽 회전
                        dir = (dir + 3) % 4
                    else: # 오른쪽 회전
                        dir = (dir + 1) % 4
            # 사과가 있을 때
            isApple = False
            for apple in apples:
                if apple[0] == nx and apple[1] == ny:
                    isApple = True
                    apples.remove((nx, ny))

            if not isApple: # 사과가 없을 때
                start_x, start_y = path[0]
                visited[start_x][start_y] = False # 몸 길이 줄이기
                path = path[1:]

            visited[nx][ny] = True
            q.append((nx, ny))
            path.append((nx, ny))
            # print(f"====={time}=====")
            # for i in visited:
            #     print(i)

bfs(0, 0)
# for i in visited:
#     print(i)
print(time+1)