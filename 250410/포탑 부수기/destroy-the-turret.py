n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

attacker_history = []

def find_attacker():
    min_bomb = 5000
    tmp = []
    row, col = 0, 0
    for j in range(m):
        for i in range(n):
            if arr[i][j] != 0 and arr[i][j] <= min_bomb:
                min_bomb = arr[i][j]
                row, col = i, j
                tmp.append((i, j))
    candidate = [bomb for bomb in tmp if arr[bomb[0]][bomb[1]] == min_bomb]
    candidate.sort(key=lambda x : (-(x[0]+x[1]), -x[1]))
    row, col = candidate[0]
    if len(candidate) > 1:
        # 공격한지 가장 최근 포탑 선정
        for i in range(len(attacker_history) - 1, -1, -1):
            for j in range(len(candidate)):
                if attacker_history[i] == candidate[j]:
                    row, col = candidate[j]
                    break
    arr[row][col] += n + m
    return row, col

def find_victim(ax, ay):
    max_bomb = 0
    tmp = []
    row, col = 0, 0
    for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if arr[i][j] != 0 and (ax != i and ay != j) and arr[i][j] >= max_bomb:
                max_bomb = arr[i][j]
                row, col = i, j
                tmp.append((i, j))
    candidate = [bomb for bomb in tmp if arr[bomb[0]][bomb[1]] == max_bomb]
    candidate.sort(key=lambda x : (x[0]+x[1], x[1]))
    
    if len(candidate) > 1:
        row, col = candidate[0]
        # 공격한지 가장 오래된 포탑 선정
        for i in range(len(attacker_history)):
            for j in range(len(candidate)):
                if attacker_history[i] == candidate[j]:
                    row, col = candidate[j]
                    break

    return row, col

# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 최단 경로 찾기
def find_route(visited, x, y, ex, ey, path):
    global min_route, min_route_len
    visited[x][y] = True
    if x == ex and y == ey:
        if len(path) < min_route_len:
            min_route_len = len(path)
            min_route = path
            return
    for i in range(4):
        # 범위 벗어나면 반대쪽으로 가도록 모듈러 적용
        nx = (x + dx[i]) % n
        ny = (y + dy[i]) % m
        if not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny] = True
            find_route(visited, nx, ny, ex, ey, path + [(nx, ny)])
            visited[nx][ny] = False

for turn in range(k):
    # 남은 포탑이 1개면 중단
    if sum([(row.count(0)) for row in arr]) == n * m - 1:
        break
    ax, ay = find_attacker()
    vx, vy = find_victim(ax, ay)
    attacker_history.append((ax, ay)) # 공격 기록 추가
    # print(ax, ay, ",", vx, vy)
    # print("맨 처음")
    # for e in arr:
    #     print(e)
    # print()

    flag = False # 가장 처음 나오는 경로로 설정하기 위한 플래그
    visited = [[False] * m for _ in range(n)]
    min_route = []
    min_route_len = int(1e9)
    find_route(visited, ax, ay, vx, vy, [(ax, ay)])
    # print(min_route)
    attacked = [(ax, ay)] # 공격과 관련 있는 포탑들
    # 레이저 공격
    if len(min_route) > 1:
        # 공격자인 첫 번째 원소 제거
        route = min_route[1:]
        for x, y in route:
            attacked.append((x, y))
            if x == vx and y == vy: # 공격 대상자 일때
                arr[x][y] -= arr[ax][ay]
                if arr[x][y] < 0:
                    arr[x][y] = 0
            else:
                arr[x][y] -= arr[ax][ay] // 2 # 그외: 절반 만큼 피해
                if arr[x][y] < 0:
                    arr[x][y] = 0
        # print("레이저 공격")
        # for e in arr:
        #     print(e)
        # print()

    else: # 포탑 공격
        arr[vx][vy] -= arr[ax][ay]
        if arr[vx][vy] < 0:
            arr[vx][vy] = 0
        attacked.append((vx, vy))
        # 시계 방향
        ddx = [-1, -1, 0, 1, 1, 1, 0, -1]
        ddy = [0, 1, 1, 1, 0, -1, -1, -1]
        for i in range(8):
            nx = (vx + ddx[i])%n
            ny = (vy + ddy[i])%m
            if arr[nx][ny] != 0 and nx != ax and ny != ay: # 공격자가 아니고, 포탑이 있을때
                arr[nx][ny] -= arr[ax][ay] // 2
                if arr[nx][ny] < 0:
                    arr[nx][ny] = 0
                attacked.append((nx, ny))
    #     print("포탑 공격")
    #     for e in arr:
    #         print(e)
    #     print()
    # print("attacked", attacked)
    # 포탑 정비
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and (i, j) not in attacked:
                arr[i][j] += 1

    # print("포탑 정비")
    # for e in arr:
    #     print(e)
    # print()
          
print(max([max(row) for row in arr]))