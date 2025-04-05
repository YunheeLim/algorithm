from collections import deque, defaultdict

n, m, f = map(int, input().split())
floor_map = []
top_left = () # 시간의벽 윗면 시작점 위치
current = [] # 타임머신 초기 위치
for i in range(n):
    row = list(map(int, input().split()))
    floor_map.append(row)
    for j in range(len(row)):
        if len(top_left) == 0 and row[j] == 3:
            top_left = (i, j)

time_map = []
side = []
for i in range(1, 5 * m + 1):
    side.append(list(map(int, input().split())))
    # 한 면 완료
    if i % m == 0:
        time_map.append(side)
        side = []

anomaly = defaultdict(list)
for _ in range(f):
    r, c, d, v = map(int, input().split())
    anomaly[v].append([r, c, d])


# for k, v in anomaly.items():
#     print(k, v)

# 시간의 벽 전개
flat_map = [[-1] * 3 * m for _ in range(3 * m)]
# 동 = 왼쪽으로 90도 회전
tmp = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        tmp[m - j - 1][i] = time_map[0][i][j]
for i in range(m, 2 * m):
    for j in range(2 * m, 3 * m):
        flat_map[i][j] = tmp[i - m][j - 2 * m]

# 서 = 오른쪽으로 90도
tmp = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        tmp[j][m - 1 - i] = time_map[1][i][j]
for i in range(m, 2 * m):
    for j in range(0, m):
        flat_map[i][j] = tmp[i - m][j]

# 남
for i in range(2 * m, 3 * m):
    for j in range(m, 2 * m):
        flat_map[i][j] = time_map[2][i - 2 * m][j - m]

# 북 = 180도 회전
tmp = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        tmp[m - 1 - i][m - 1 - j] = time_map[3][i][j]
for i in range(0, m):
    for j in range(m, 2 * m):
        flat_map[i][j] = tmp[i][j - m]     

# 위
for i in range(m, 2 * m):
    for j in range(m, 2 * m):
        flat_map[i][j] = time_map[4][i - m][j - m]
        if flat_map[i][j] == 2: # 타임머신 초기 위치 저장
            current.append((i, j))

# for e in flat_map:
#     print(e)

# 동서남북 중 어느 면에 있는지 확인
def check_side(x, y):
    if m <= x < 2 * m and 2 * m <= y < 3 * m: # 동
        return 0
    elif m <= x < 2 * m and 0 <= y < m: # 서
        return 1
    elif 2 * m <= x < 3 * m and m <= y < 2 * m: # 남
        return 2
    elif 0 <= x < m and m <= y < 2 * m: # 북
        return 3

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited_turn = set()

# 옆면 이동 함수
def move_side(x, y):
    nx, ny = -1, -1
    if check_side(x, y) == 0: # 동
        if x == m: # 동 -> 북
            nx = (3 * m - y - 1)
            ny = 2 * m - 1
        elif x == 2 * m - 1: # 동 -> 남
            nx = 3 * m - 1 - (3 * m - y - 1)
            ny = 2 * m - 1
    elif check_side(x, y) == 1: # 서
        if x == m: # 서 -> 북
            nx = y
            ny = m
        elif x == 2 * m - 1: # 서 -> 남
            nx = (3 * m - y - 1)
            ny = m
    elif check_side(x, y) == 2: # 남
        if y == 2 * m - 1: # 남 -> 동
            nx = 2 * m - 1
            ny = 3 * m - 1 - (3 * m - x - 1)
        elif y == m: # 남 -> 서
            nx = 2 * m - 1
            ny = (3 * m - x - 1)
    elif check_side(x, y) == 3: # 북
        if y == 2 * m - 1: # 북 -> 동
            nx = m
            ny = 3 * m - x - 1
        elif y == m: # 북 -> 서
            nx = m
            ny = x

    return (nx, ny)

def bfs(x, y):
    time[x][y] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 3 * m and 0 <= ny < 3 * m:

                if time[nx][ny] > time[x][y] + 1:
                    if flat_map[nx][ny] == 0:
                        time[nx][ny] = time[x][y] + 1
                        q.append((nx, ny))

                    elif flat_map[nx][ny] == -1: # 옆면 이동
                        nx, ny = move_side(x, y)
                        
                        if flat_map[nx][ny] == 0:
                            if time[nx][ny] > time[x][y] + 1:
                                time[nx][ny] = time[x][y] + 1
                                q.append((nx, ny))

time = [[int(1e9)] * 3 * m for _ in range(3 * m)] 
bfs(current[0][0], current[0][1])

# for row in time:
#     for j in row:
#         print(f"{j:<10}", end="\t")
#     print()

# print('top_left: ', top_left)

time_floor = [[int(1e9)] * n for _ in range(n)]

# 시간의벽에서 바닥 간 통로 찾기
path = ()
ith = -1
jth = -1
for i in range(top_left[0] - 1, top_left[0] + m + 1):
    ith += 1
    for j in range(top_left[1] - 1, top_left[1] + m + 1):
        jth += 1
        if floor_map[i][j] == 0:
            path = (i, j)
            # 틀리면 동쪽 말고도 나머지 잘 되는지 확인 필요
            if j == top_left[1] + m: # 동
                time_floor[i][j] = time[m + ith - 1][3 * m - 1] + 1
            elif j == top_left[1] - 1: # 서
                time_floor[i][j] = time[m + ith - 1][0] + 1
            elif i == top_left[0] + m: # 남
                time_floor[i][j] = time[3 * m - 1][m + jth - 1] + 1
            elif i == top_left[0] - 1: # 북
                time_floor[i][j] = time[0][m + jth - 1] + 1
    jth = -1

ans = -1

def bfs2(x, y):
    global ans
    # 엣지케이스: 탈출구가 연결 통로인 경우
    if floor_map[x][y] == 4:
        ans = time_floor[x][y]
        return
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if floor_map[nx][ny] == 4:
                    time_floor[nx][ny] = time_floor[x][y] + 1
                    ans = time_floor[nx][ny]
                    return
                # 이상현상이 바닥에서 시간벽으로 이동할 경우 고려 필요!!
                turn = time_floor[x][y] + 1
                for v in anomaly:
                    if (turn % v == 0):
                        for idx, val in enumerate(anomaly[v]):
                            r, c, d = val
                            if turn not in visited_turn:
                                visited_turn.add(turn)
                                floor_map[r][c] = 1
                                nr = r + dx[d]
                                nc = c + dy[d]
                                if 0 <= nr < n and 0 <= nc < n and floor_map[nr][nc] == 0: # 이상현상 이동
                                    floor_map[nr][nc] = 1                       

                if floor_map[nx][ny] == 0 and time_floor[nx][ny] > time_floor[x][y] + 1:
                    time_floor[nx][ny] = time_floor[x][y] + 1
                    q.append((nx, ny))

bfs2(path[0], path[1])
# print(ans)
# for e in time_floor:
#     print(e)

print(ans)
