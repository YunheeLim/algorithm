n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
people_pos = []
people_arr = [[[] for _ in range(n)] for _ in range(n)]
people_cnt = m
for idx in range(m):
    a, b = map(int, input().split())
    people_pos.append([a - 1, b - 1, 100, idx])
    people_arr[a - 1][b - 1].append((idx))
ex, ey = map(int, input().split())
ex -= 1
ey -= 1

# print("===origin people===")
# for e in people_arr:
#     print(e)

def get_min_dist(sx, sy, ex, ey):
    return abs(sx - ex) + abs(sy - ey)

def move(x, y, ex, ey):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 벽이 아니고
        if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0:
            # 출구까지의 거리가 감소할때
            if get_min_dist(nx, ny, ex, ey) < get_min_dist(x, y, ex, ey):
                return nx, ny, get_min_dist(nx, ny, ex, ey)
    return x, y, get_min_dist(x, y, ex, ey)

def make_rectangle(dist, sx, sy, ex, ey):
    side = dist + 1
    candidates = []

    # (r1, c1) = 정사각형의 좌측 상단
    for r1 in range(n - side + 1):
        for c1 in range(n - side + 1):
            r2 = r1 + side - 1
            c2 = c1 + side - 1

            # sx, sy 와 ex, ey 가 모두 포함되어야 함
            if (r1 <= sx <= r2 and c1 <= sy <= c2 and
                r1 <= ex <= r2 and c1 <= ey <= c2):
                candidates.append((r1, c1, r2, c2))

    if not candidates:
        return False  # 만들 수 있는 정사각형 없음

    # 조건: r이 가장 작고, 같다면 c가 가장 작은 것
    candidates.sort()
    r1, c1, r2, c2 = candidates[0]
    return side, r1, c1, r2, c2

def rotate(side, sx, sy, endx, endy):
    global ex, ey

    rotated_arr = [[0] * side for _ in range(side)]
    rotated_people_arr = [[[] for _ in range(side)] for _ in range(side)]

    # 출구가 정사각형 안에 있을 때만 회전
    if sx <= ex <= sx + side - 1 and sy <= ey <= sy + side - 1:
        local_ex = ex - sx
        local_ey = ey - sy

        rotated_ex = local_ey
        rotated_ey = side - 1 - local_ex

        ex = sx + rotated_ex
        ey = sy + rotated_ey

    # 회전 수행
    for i in range(side):
        for j in range(side):
            gi, gj = sx + i, sy + j
            ri = j
            rj = side - 1 - i

            rotated_arr[ri][rj] = maze[gi][gj] - 1 if maze[gi][gj] != 0 else 0
            rotated_people_arr[ri][rj] = people_arr[gi][gj][:]

    # 회전 결과 반영
    for i in range(side):
        for j in range(side):
            gi, gj = sx + i, sy + j
            maze[gi][gj] = rotated_arr[i][j]
            people_arr[gi][gj] = rotated_people_arr[i][j][:]

    # 사람 위치 업데이트
    for i in range(n):
        for j in range(n):
            if people_arr[i][j]:
                for person in people_arr[i][j]:
                    people_pos[person] = [i, j, abs(i - ex) + abs(j - ey), person]

    return ex, ey

answer = 0
for turn in range(k):
    # print()
    # print()
    # print('[turn]', turn)
    # print()

    # print("현재 사람들 위치:", people_pos)

    # 모든 참가자가 미로 탈출
    if people_cnt == 0:
        break

    # 참가자 이동
    updated_people_pos = []
    updated_people_arr = [[[] for _ in range(n)] for _ in range(n)]
    for idx in range(len(people_pos)):
        if people_pos[idx][0] != -1:
            prev_x, prev_y = people_pos[idx][0], people_pos[idx][1] # 이동했는지 확인용
            people_pos[idx][0], people_pos[idx][1], people_pos[idx][2] = move(people_pos[idx][0], people_pos[idx][1], ex, ey)
            if prev_x != people_pos[idx][0] or prev_y != people_pos[idx][1]: # 이동했으면 정답에 추가
                answer += 1
            updated_people_arr[people_pos[idx][0]][people_pos[idx][1]].append(idx)
        # 출구에 도착한 참가자 있으면 탈출
        if people_pos[idx][0] == ex and people_pos[idx][1] == ey:
            updated_people_arr[ex][ey].remove(idx)
            people_pos[idx] = [-1, -1, 100, idx]
            people_cnt -= 1
        # else:
        #     updated_people_pos.append([people_pos[idx][0], people_pos[idx][1], people_pos[idx][2], people_pos[idx][3]])

    people_arr = [row[:] for row in updated_people_arr]
    # print("===사람들 이동===")
    # for e in people_arr:
    #     print(e)
    # print('kajhf', people_pos)

    # 출구와 가까운 순으로 정렬
    tmp = [row[:] for row in people_pos]
    tmp.sort(key=lambda x: x[2])
    candidate_people = [people for people in tmp if people[2] == tmp[0][2] and people[0] != -1]
    # print('candidate_people', candidate_people)
    candidate_rect = []
    for candi in candidate_people:
        idx = candi[3]
        if make_rectangle(people_pos[idx][2], people_pos[idx][0], people_pos[idx][1], ex, ey) != False: # 사각형이 범위 넘어가지 않을때
            candidate_rect.append(make_rectangle(people_pos[idx][2], people_pos[idx][0], people_pos[idx][1], ex, ey))
    candidate_rect.sort()
    selected_rect_start = candidate_rect[0]
    ex, ey = rotate(selected_rect_start[0], selected_rect_start[1], selected_rect_start[2], selected_rect_start[3], selected_rect_start[4])
    # print('selected start:', selected_rect_start)
    
    # print("===rotate arr===")
    # for e in maze:
    #     print(e)
    # print('===rotate people===')
    # for e in people_arr:
    #     print(e)
    # print('업데이트 된 출구:', ex, ey)

print(answer)
print(ex + 1, ey + 1)