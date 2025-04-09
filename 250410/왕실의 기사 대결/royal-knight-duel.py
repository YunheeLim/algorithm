from collections import deque

l, n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(l)]
fall_info = [row[:] for row in arr]
people = [[-1, -1, -1, -1, -1]]
people_power = [0] # 각 기사들 체력
for _ in range(n):
    people.append(list(map(int, input().split())))
    people_power.append(people[-1][-1])
commands = [list(map(int, input().split())) for _ in range(q)]

# 기사 번호가 벽/함정과 겹치지 않게 음수로 표시
people_pos = [[] for _ in range(len(people) + 1)]
for idx in range(1, len(people)):
    r, c, h, w, k = people[idx]
    for i in range(r - 1, r - 1 + h):
        for j in range(c - 1, c - 1 + w):
            arr[i][j] = -idx
            people_pos[idx].append([i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < l and 0 <= y < l

def get_candidate(idx, direction):
    candidate = set() # 일직선상에 있는 밀릴 기사들 후보
    candidate.add(idx) # 시작 기사는 무조건 추가

    q = deque([idx])
    while q:
        knight = q.popleft()
        rows = set() # 시작 기사의 모든 행
        cols = set() # 시작 기사의 모든 열
        for x, y in people_pos[knight]:
            rows.add(x)
            cols.add(y)
        rows = list(rows)
        rows.sort()
        cols = list(cols)
        cols.sort()

        if direction == 0:
            for col in cols:
                if not in_range(rows[0] - 1, col) or arr[rows[0] - 1][col] == 2: # 벽 만남
                    return {}
                if in_range(rows[0] - 1, col) and arr[rows[0] - 1][col] < 0: # 기사가 맞닿아 있을 때
                    candidate.add(-arr[rows[0] - 1][col])
                    q.append(-arr[rows[0] - 1][col])
        elif direction == 1: # 우
            for row in rows:
                if not in_range(row, cols[-1] + 1) or arr[row][cols[-1] + 1] == 2: # 벽 만남
                    return {}
                if in_range(row, cols[-1] + 1) and arr[row][cols[-1] + 1] < 0: # 기사가 맞닿아 있을 때
                    candidate.add(-arr[row][cols[-1] + 1])
                    q.append(-arr[row][cols[-1] + 1])
        elif direction == 2: # 하
            for col in cols:
                if not in_range(rows[-1] + 1, col) or arr[rows[-1] + 1][col] == 2: # 벽 만남
                    return {}
                if in_range(rows[-1] + 1, col) and arr[rows[-1] + 1][col] < 0: # 기사가 맞닿아 있을 때
                    candidate.add(-arr[rows[-1] + 1][col])
                    q.append(-arr[rows[-1] + 1][col])
        elif direction == 3: # 좌
            for row in rows:
                if not in_range(row, cols[0] - 1) or arr[row][cols[0] - 1] == 2: # 벽 만남
                    return {}
                if in_range(row, cols[0] - 1) and arr[row][cols[0] - 1] < 0: # 기사가 맞닿아 있을 때
                    candidate.add(-arr[row][cols[0] - 1])
                    q.append(-arr[row][cols[0] - 1])

    return candidate

answer = 0
people_damaged = [0] * len(people)
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
        if candi == idx: # 명령 받은 기사 제외
            continue
        remain = people_power[candi] # 체력
        for x, y in people_pos[candi]:
            arr[x][y] = -candi
            # 데미지
            if fall_info[x][y] == 1: # 함정
                people_power[candi] -= 1
                people_damaged[candi] += 1
                answer += 1

    # 체력 음수인 기사 제거
    for candi in candidates:
        if people_power[candi] < 0: # 사라짐
            for x, y in people_pos[candi]:
                arr[x][y] = 0
                people_pos[candi] = [-1, -1, -1, -1, -1]
                people_power[candi] = -1
                answer -= people_damaged[candi]
    
    # for e in arr:
    #     print(e)

print(answer)