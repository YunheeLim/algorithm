from collections import deque

n, m = map(int, input().split())
base_camp = [list(map(int, input().split())) for _ in range(n)]
people_pos = [[int(1e9), int(1e9)]] # 사람들의 위치 (사람, 편의점, 베이스캠프의 인덱스는 1부터 시작)
conv_pos = [(int(1e9), int(1e9), 0)] # (행, 열, 편의점 인덱스)

# 편의점 위치에 인덱스로 저장
conv = [[0] * n for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    people_pos.append([int(1e9), int(1e9)])
    conv[x - 1][y - 1] = i + 1
    conv_pos.append((x - 1, y - 1, i + 1))

# 갈 수 있는 칸인지 저장하는 배열
can_go = [[True] * n for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 편의점과 가장 가까운 베이스 캠프 찾기 (정해진 베이스캠프 고려 필요)
for x, y, idx in conv_pos:
    if idx == 0:
        continue
    visited = [[int(1e9)] * n for _ in range(n)]
    min_dist = int(1e9)
    candidate = [] # 가장 가까운 베이스캠프 후보
    q = deque([(x, y)])
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                if base_camp[nx][ny] == 1 and visited[nx][ny] <= min_dist:
                    min_dist = visited[nx][ny]
                    candidate.append((nx, ny))
                q.append((nx, ny))
    candidate.sort()
    x, y = candidate[0] # 가장 가까운 베이스 캠프
    base_camp[x][y] = -idx # 베이스캠프 유무(0/1)과 겹치기 않게 하기 위해 편의점 인덱스를 음수로 저장

# for e in conv:
#     print(e)
# print()
# for e in base_camp:
#     print(e)

# 매번 찾아야함
def find_route(sx, sy, ex, ey, idx):
    visited = [[int(1e9)] * n for _ in range(n)]
    q = deque([(sx, sy, [])])
    visited[sx][sy] = 0
    while q:
        x, y, path = q.popleft()
        # 편의점 도착
        if x == ex and y == ey:
            return path
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > visited[x][y] + 1 and can_go[nx][ny] == True:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny, path + [(nx, ny)]))

def find_base_camp_pos(idx):
    for i in range(n):
        for j in range(n):
            if base_camp[i][j] == -idx:
                return i, j
            
def check_end():
    for idx in range(1, len(people_pos)):
        if idx == 0:
            continue
        if people_pos[idx][0] != conv_pos[idx][0] or people_pos[idx][1] != conv_pos[idx][1]:
            return False
    return True

# 움직임 진행(총 m번)
answer = 1
while True:
    # print('turn', answer)
    if check_end() == True:
        break
    will_disable = [] # 이동불가할 지점 저장 (2명 이상이 이동할 경우 대비)
    for idx in range(1, len(people_pos)):
        # 격자 밖에 있고, answer번째 사람일때
        if people_pos[idx] == [int(1e9), int(1e9)] and idx == answer:
            x, y = find_base_camp_pos(idx)
            # 방문 불가 처리
            can_go[x][y] = False
            # 사람 위치 갱신
            people_pos[idx][0] = x
            people_pos[idx][1] = y
        # 편의점에 도착했을 때
        elif people_pos[idx][0] == conv_pos[idx][0] and people_pos[idx][1] == conv_pos[idx][1]:
            # 방문 불가 처리
            can_go[people_pos[idx][0]][people_pos[idx][1]] = False
            # 사람 위치 갱신
            people_pos[idx][0] = conv_pos[idx][0]
            people_pos[idx][1] = conv_pos[idx][1]
        # 격자 안에 있을 때
        elif people_pos[idx] != [int(1e9), int(1e9)]: # 두명이 한 칸에 있을 때 모두 움직이고 방문 불가 처리 하도록!!
            px, py = people_pos[idx][0], people_pos[idx][1]
            cx, cy = conv_pos[idx][0], conv_pos[idx][1]
            route = find_route(px, py, cx, cy, idx)
            people_pos[idx] = [route[0][0], route[0][1]]
            if (route[0][0], route[0][1]) not in will_disable:
                will_disable.append((route[0][0], route[0][1]))
    for x, y in will_disable:
        can_go[x][y] = False

    # print('check end:', check_end())
    # print('편의점 위치:', conv_pos)
    # print('사람들 이동한 위치:', people_pos)
    # print('===이동 불가 지역 확인===')
    # for e in can_go:
    #     print(e)
    # print('======')
    answer += 1
# print(people_pos)
# print(conv_pos)
print(answer - 1)
