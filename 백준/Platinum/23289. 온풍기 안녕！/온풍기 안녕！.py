import sys
from collections import deque
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = []
heaters = set()
inspection = set()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(r):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(c):
        if row[j] == 5:
            inspection.add((i, j))
            arr[i][j] = 0
        elif row[j] != 5 and row[j] != 0:
            heaters.add((i, j, row[j] - 1))
            arr[i][j] = 0

w = int(input())
walls = set() # 양방향
for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        # 양방향으로 저장
        walls.add((x, y, x - 1, y))
        walls.add((x - 1, y, x, y))
    else:
        walls.add((x, y, x, y + 1))
        walls.add((x, y + 1, x, y))

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def check_wall(x, y, nx, ny, dir):
    if dir == 0: # 오
        if nx == x: # 바로 오
            return (x, y, x, y + 1) in walls
        elif nx == x - 1: # 위쪽 오
            return (x, y, x - 1, y) in walls or (x - 1, y, x - 1, y + 1) in walls
        elif nx == x + 1: # 아래쪽 오
            return (x, y, x + 1, y) in walls or (x + 1, y, x + 1, y + 1) in walls
    elif dir == 1: # 왼
        if nx == x: # 바로 왼
            return (x, y, x, y - 1) in walls
        elif nx == x - 1: # 위쪽 왼
            return (x, y, x - 1, y) in walls or (x - 1, y, x - 1, y - 1) in walls
        elif nx == x + 1: # 아래쪽 오
            return (x, y, x + 1, y) in walls or (x + 1, y, x + 1, y - 1) in walls
    elif dir == 2: # 위
        if ny == y: # 바로 위
            return (x, y, x - 1, y) in walls
        elif ny == y - 1: # 왼쪽 위
            return (x, y, x, y - 1) in walls or (x, y - 1, x - 1, y - 1) in walls
        elif ny == y + 1: # 오른쪽 위
            return (x, y, x, y + 1) in walls or (x, y + 1, x - 1, y + 1) in walls
    elif dir == 3: # 아래
        if ny == y: # 바로 아래
            return (x, y, x + 1, y) in walls
        elif ny == y - 1: # 왼쪽 아래
            return (x, y, x, y - 1) in walls or (x, y - 1, x + 1, y - 1) in walls
        elif ny == y + 1: # 오른쪽 아래
            return (x, y, x, y + 1) in walls or (x, y + 1, x + 1, y + 1) in walls
    return False

# 온도 상승
def windows(x, y, dir):
    x = x + dx[dir]
    y = y + dy[dir]
    temper = 5
    arr[x][y] += temper
    visited[x][y] = True
    q = deque([(x, y, temper - 1)])
    while q:
        if temper == 0:
            break
        x, y, temper = q.popleft()
        if dir == 0: # 오
            for i in [x - 1, x, x + 1]:
                if in_range(i, y + 1) and not visited[i][y + 1]:
                    if check_wall(x, y, i, y + 1, dir) == False: # 벽 체크
                        arr[i][y + 1] += temper
                        visited[i][y + 1] = True
                        q.append((i, y + 1, temper - 1))
        elif dir == 1: # 왼
            for i in [x - 1, x, x + 1]:
                if in_range(i, y - 1) and not visited[i][y - 1]:
                    if check_wall(x, y, i, y - 1, dir) == False: # 벽 체크
                        arr[i][y - 1] += temper
                        visited[i][y - 1] = True
                        q.append((i, y - 1, temper - 1))
        elif dir == 2: # 위
            for j in [y - 1, y, y + 1]:
                if in_range(x - 1, j) and not visited[x - 1][j]:
                    if check_wall(x, y, x - 1, j, dir) == False: # 벽 체크
                        arr[x - 1][j] += temper
                        visited[x - 1][j] = True
                        q.append((x - 1, j, temper - 1))
        elif dir == 3: # 아래
            for j in [y - 1, y, y + 1]:
                if in_range(x + 1, j) and not visited[x + 1][j]:
                    if check_wall(x, y, x + 1, j, dir) == False: # 벽 체크
                        arr[x + 1][j] += temper
                        visited[x + 1][j] = True
                        q.append((x + 1, j, temper - 1))

# 온도 조절
def control():
    total_temper = [[0] * c for _ in range(r)] # 최종 온도 변화값
    # 총 온도 변화 계산
    for x in range(r):
        for y in range(c):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if in_range(nx, ny) and arr[x][y] > arr[nx][ny]:
                    if check_wall(x, y, nx, ny, i) == False:
                        diff = (arr[x][y] - arr[nx][ny]) // 4
                        total_temper[x][y] -= diff
                        total_temper[nx][ny] += diff
    # print("==total temper===")
    # for e in total_temper:
    #     print(e)
    # 온도 적용
    for i in range(r):
        for j in range(c):
            arr[i][j] += total_temper[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

def lower_side():
    for i in [0, r - 1]:
        for j in range(c):
            if arr[i][j] - 1 >= 0:
                arr[i][j] -= 1

    for j in [0, c - 1]:
        for i in range(1, r - 1):
            if arr[i][j] - 1 >= 0:
                arr[i][j] -= 1

def check_inspection():
    for x, y in inspection:
        if arr[x][y] < k:
            return False
    return True

chocolate = 0
while True:
    for x, y, dir in heaters:
        visited = [[False] * c for _ in range(r)]
        windows(x, y, dir)

    control()
    lower_side()
    chocolate += 1
    if check_inspection():
        break

    if chocolate > 100:
        break


print(chocolate)

# print("==========")
# for e in arr:
#     print(e)
# print('inspection:', inspection)
# print('heaters:', heaters)
# print('walls:', walls)