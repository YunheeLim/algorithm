from collections import deque

l, n, q = map(int, input().split())
fall_info = [list(map(int, input().split())) for _ in range(l)] # 벽, 함정 배열
arr = [[0] * l for _ in range(l)] # 기사 배열
people_pos = [[] for _ in range(n + 1)] # 각 기사 좌표
people_power = [0] # 각 기사 체력

# 기사 배열에 기사 표시
for idx in range(1, n + 1):
    r, c, h, w, k = map(int, input().split())
    for i in range(r - 1, r - 1 + h):
        for j in range(c - 1, c - 1 + w):
            arr[i][j] = idx
            people_pos[idx].append([i, j])
    people_power.append(k)

commands = [list(map(int, input().split())) for _ in range(q)] # 명령

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 체스판 내에 있는지 확인
def in_range(x, y):
    return 0 <= x < l and 0 <= y < l

# 밀릴 예정인 기사들 반환 함수
def get_candidate(idx, direction):
    candidate = set() # 일직선상에 있는 밀릴 기사들 후보
    candidate.add(idx) # 시작 기사는 무조건 추가

    q = deque([idx])
    # 현재 기사와 연결된 기사 모두 큐에 추가 (상하좌우에 따라 조건 다름)
    while q:
        knight = q.popleft() # 현재 기사
        rows = set() # 시작 기사의 모든 행
        cols = set() # 시작 기사의 모든 열
        for x, y in people_pos[knight]:
            rows.add(x)
            cols.add(y)
        rows = list(rows)
        rows.sort()
        cols = list(cols)
        cols.sort()

        if direction == 0: # 상
            for col in cols:
                if not in_range(rows[0] - 1, col) or fall_info[rows[0] - 1][col] == 2: # 벽 만나면 모두 이동 불가
                    return {}
                if in_range(rows[0] - 1, col) and arr[rows[0] - 1][col] > 0: # 기사가 맞닿아 있을 때
                    candidate.add(arr[rows[0] - 1][col])
                    q.append(arr[rows[0] - 1][col])
        elif direction == 1: # 우
            for row in rows:
                if not in_range(row, cols[-1] + 1) or fall_info[row][cols[-1] + 1] == 2: # 벽 만나면 모두 이동 불가
                    return {}
                if in_range(row, cols[-1] + 1) and arr[row][cols[-1] + 1] > 0: # 기사가 맞닿아 있을 때
                    candidate.add(arr[row][cols[-1] + 1])
                    q.append(arr[row][cols[-1] + 1])
        elif direction == 2: # 하
            for col in cols:
                if not in_range(rows[-1] + 1, col) or fall_info[rows[-1] + 1][col] == 2: # 벽 만나면 모두 이동 불가
                    return {}
                if in_range(rows[-1] + 1, col) and arr[rows[-1] + 1][col] > 0: # 기사가 맞닿아 있을 때
                    candidate.add(arr[rows[-1] + 1][col])
                    q.append(arr[rows[-1] + 1][col])
        elif direction == 3: # 좌
            for row in rows:
                if not in_range(row, cols[0] - 1) or fall_info[row][cols[0] - 1] == 2: # 벽 만나면 모두 이동 불가
                    return {}
                if in_range(row, cols[0] - 1) and arr[row][cols[0] - 1] > 0: # 기사가 맞닿아 있을 때
                    candidate.add(arr[row][cols[0] - 1])
                    q.append(arr[row][cols[0] - 1])

    return candidate

people_damaged = [0] * len(people_pos) # 각 기사가 받은 데미지

for idx, d in commands:
    # 사라진 기사일 경우 제외
    if people_power[idx] == -1:
        continue

    candidates = get_candidate(idx, d)

    # 밀린 좌표 업데이트 및 기존 자리 삭제
    for candi in candidates:
        updated_pos = []
        for x, y in people_pos[candi]:
            arr[x][y] = 0
            updated_pos.append([x + dx[d], y + dy[d]])
        people_pos[candi] = [row[:] for row in updated_pos]

    # 밀린 좌표로 자리 표시
    for candi in candidates:
        remain = people_power[candi] # 체력
        for x, y in people_pos[candi]:
            arr[x][y] = candi
            # 데미지
            if fall_info[x][y] == 1: # 함정
                if candi != idx: # 명령 받은 기사 제외
                    people_damaged[candi] += 1
                    people_power[candi] -= 1

    # 체력 음수인 기사 제거
    for candi in candidates:
        if people_power[candi] <= 0: # 사라짐
            for x, y in people_pos[candi]:
                arr[x][y] = 0
                people_pos[candi] = [-1, -1]
                people_power[candi] = -1
                people_damaged[candi] = -1

# 사라진 기사들 제외 데미지 총합 출력
answer = 0
for damage in people_damaged:
    if damage != -1:
        answer += damage
print(answer)