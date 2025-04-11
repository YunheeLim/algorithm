n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# 참가자 위치 정보: [x, y, 출구까지의 거리, 인덱스]
people_pos = [[a - 1, b - 1, 100, idx] for idx, (a, b) in enumerate([tuple(map(int, input().split())) for _ in range(m)])]

# 격자 내 참가자 배치 상태
people_arr = [[[] for _ in range(n)] for _ in range(n)]
for person in people_pos:
    x, y = person[0], person[1]
    people_arr[x][y].append(person[3])

# 출구 위치 (0-indexed)
ex, ey = map(lambda x: int(x) - 1, input().split())

def get_min_dist(sx, sy, ex, ey):
    """맨해튼 거리 반환"""
    return abs(sx - ex) + abs(sy - ey)

def move(x, y, ex, ey):
    """출구와 가까워지는 방향으로 1칸 이동"""
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # 상하좌우
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0:
            if get_min_dist(nx, ny, ex, ey) < get_min_dist(x, y, ex, ey):
                return nx, ny, get_min_dist(nx, ny, ex, ey)
    return x, y, get_min_dist(x, y, ex, ey)

def make_rectangle(dist, sx, sy, ex, ey):
    """출구와 참가자 1명 이상을 포함하는 가장 작은 정사각형 찾기"""
    dist += 1  # side = 거리 + 1
    for sz in range(2, dist + 1):  # 가능한 정사각형 크기
        for x1 in range(n - sz + 1):
            for y1 in range(n - sz + 1):
                x2, y2 = x1 + sz - 1, y1 + sz - 1
                if not (x1 <= ex <= x2 and y1 <= ey <= y2):
                    continue
                for tx, ty, *_ in people_pos:
                    if x1 <= tx <= x2 and y1 <= ty <= y2 and (tx != ex or ty != ey):
                        return sz, x1, y1, x2, y2
    return False

def rotate(side, sx, sy, endx, endy):
    """정사각형 회전 + 출구 위치 업데이트 + 사람 위치 업데이트"""
    global ex, ey

    # 회전 임시 배열
    rotated_maze = [[0] * side for _ in range(side)]
    rotated_people = [[[] for _ in range(side)] for _ in range(side)]

    # 출구가 정사각형 내에 있을 경우 회전
    if sx <= ex <= sx + side - 1 and sy <= ey <= sy + side - 1:
        lx, ly = ex - sx, ey - sy
        ex, ey = sx + ly, sy + side - 1 - lx

    # 회전 처리
    for i in range(side):
        for j in range(side):
            gi, gj = sx + i, sy + j
            ri, rj = j, side - 1 - i
            rotated_maze[ri][rj] = max(maze[gi][gj] - 1, 0) if maze[gi][gj] else 0
            rotated_people[ri][rj] = people_arr[gi][gj][:]

    # 회전 결과 적용
    for i in range(side):
        for j in range(side):
            gi, gj = sx + i, sy + j
            maze[gi][gj] = rotated_maze[i][j]
            people_arr[gi][gj] = rotated_people[i][j][:]

    # 참가자 위치 정보 업데이트
    for i in range(n):
        for j in range(n):
            for person in people_arr[i][j]:
                people_pos[person] = [i, j, get_min_dist(i, j, ex, ey), person]

    return ex, ey

# =========================== 시뮬레이션 시작 ============================

answer = 0
people_cnt = m

for _ in range(k):
    if people_cnt == 0:
        break

    # 참가자 이동 처리
    next_people_arr = [[[] for _ in range(n)] for _ in range(n)]
    for idx, (x, y, _, _) in enumerate(people_pos):
        if x == -1:
            continue
        nx, ny, dist = move(x, y, ex, ey)
        people_pos[idx][:3] = [nx, ny, dist]
        next_people_arr[nx][ny].append(idx)
        if (nx, ny) != (x, y):  # 실제 이동 시 카운트 증가
            answer += 1
        if nx == ex and ny == ey:  # 출구 도착
            people_pos[idx] = [-1, -1, 100, idx]
            people_cnt -= 1
            next_people_arr[nx][ny].remove(idx)

    people_arr = next_people_arr

    if people_cnt == 0:
        break

    # 출구와 가장 가까운 사람 기준으로 정사각형 선택
    candidate_people = sorted([p for p in people_pos if p[0] != -1], key=lambda x: x[2])
    min_dist = candidate_people[0][2]
    rects = []

    for person in candidate_people:
        if person[2] != min_dist:
            break
        rect = make_rectangle(person[2], person[0], person[1], ex, ey)
        if rect:
            rects.append(rect)

    if rects:
        rects.sort()  # 좌상단 기준 우선
        ex, ey = rotate(*rects[0])  # 회전

# =========================== 결과 출력 ============================
print(answer)
print(ex + 1, ey + 1)  # 1-indexed 출력
