from collections import deque

k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
nums = list(map(int, input().split()))
# 북 남 동 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# 행렬 회전 함수
def rotate(grid, degree):
    result = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(3):
        for j in range(3):
            if degree == 1: # 90도
                result[j][3 - 1 - i] = grid[i][j]
            elif degree == 2: # 180도
                result[3 - 1 - i][3 - 1 - j] = grid[i][j]
            elif degree == 3: # 270도
                result[3 - 1 - j][i] = grid[i][j]
    return result

# 연결 요소 개수 세기
def dfs(grid, x, y, visited, path):
    visited[x][y] = True
    path.append((x, y))
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
                c, p = dfs(grid, nx, ny, visited, path)
                cnt += c
    return cnt, path

# 유물 가치 계산
def get_max_val(grid):
    max_val = 0
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                # 유물 삭제를 위해 기록 저장
                path = []
                # print('위치:', i, j, "값:", grid[i][j], "연결조각개수:", dfs(grid, i, j, visited))
                val, result_path = dfs(grid, i, j, visited, path)
                if val >= 3: # 유물 완성
                    max_val += val
                    # 유물 삭제
                    for x, y in path:
                        grid[x][y] = -1
    return max_val

# 벽면의 숫자가 채워지기 시작하는 지점 찾는 함수 (한 덩어리에 대해서만)
def find_start(grid, x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    min_x, min_y = x, y  # 시작 지점 초기화

    while q:
        cx, cy = q.popleft()

        # 좌상단 우선 기준 갱신
        if cy < min_y or (cy == min_y and cx > min_x):
            min_x, min_y = cx, cy

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if grid[nx][ny] == grid[cx][cy] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return (min_x, min_y)

# 벽면의 숫자가 채워지기 시작하는 지점들 찾는 함수 (여러 덩어리에 대해서)
def find_start_points(grid):
    start_points = []
    visited2 = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            # 사라진 덩어리가 여러개 있을 수 있기 때문에 시작지점들 배열로 저장
            if selected_arr[i][j] == -1 and not visited2[i][j]:
                start_x, start_y = find_start(selected_arr, i, j, visited2)
                start_points.append((start_x, start_y))
    # 열이 가장 작고 행이 가장 큰 곳 순으로 정렬
    start_points.sort(key=lambda x: (-x[0], x[1]))
    return start_points

# 벽면의 숫자 채우기 (북-남-동 순서 보장 위해 bfs로 진행)
def fill(grid, x, y, idx):
    q = deque([(x, y)])
    grid[x][y] = nums[idx]
    idx += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and grid[nx][ny] == -1:
                grid[nx][ny] = nums[idx]
                if idx < len(nums) - 1:
                    idx += 1
                q.append((nx, ny))
    return idx

flag = True # 탐사 진행 가능 여부
wall_idx = 0 # 현재 가리키고 있는 벽면 숫자의 인덱스
turn = 0
while turn < k and flag:
    flag = True
    answer = 0 # 각 턴마다의 유물 가치
    # ==== 탐사 진행 시작 ====
    # 중심점 지정
    candidate = [] # 유물 가치 최대가 되는 배열 후보(유물가치, 배열, 회전각도, 회전중심열, 회전중심행)
    max_value = 0 # 최대 유물 가치
    for r in range(0, 3):
        for c in range(0, 3):
            # 배열 슬라이싱
            tmp = []
            for i in range(r, r + 3):
                row = []
                for j in range(c, c + 3):
                    row.append(arr[i][j])
                tmp.append(row)

            # print('중심점', r, c)

            # 3방향 회전
            rotated_tmp = []
            for degree in range(1, 4):
                rotated_tmp = rotate(tmp, degree)
                # 원래 배열에 합치기, 복사본으로
                copy_arr = [row[:] for row in arr]
                for rr in range(r, r + 3):
                    for cc in range(c, c + 3):
                        copy_arr[rr][cc] = rotated_tmp[rr - r][cc - c]
                # 변경 적용한 배열 확인
                # print('회전각도:', degree * 90)
                # for v in copy_arr:
                #     print(v)
                # print('유물 가치', get_max_val(copy_arr))
                get_max_value = get_max_val(copy_arr)
                if get_max_value >= max_value:
                    candidate.append([get_max_value, copy_arr, degree, c, r])


    candidate.sort(key=lambda x: (-x[0], x[2], x[3], x[4]))
    # 유물가치가 3개 이상 되는 경우가 없을 경우 탐사 중단
    if candidate[0][0] < 3:
        flag = False
        break
    selected_arr = candidate[0][1] # 유물가치가 최대가 되도록 회전한 배열
    #선택된 배열 확인
    # if turn == 2:
    # print("===selected===")
    # for e in selected_arr:
    #     print(e) 
    # print("======")
        # break
    # ==== 탐사 진행 끝 ====

    # ==== 유물 1차 획득 시작 ====
    removed = candidate[0][0] # 사라진 조각 개수
    answer += removed

    start_points = find_start_points(selected_arr)

    # print('===시작지점들===')
    # for x, y in start_points:
    #     print(x, y)
    # print('======')

    for start_x, start_y in start_points:
        wall_idx = fill(selected_arr, start_x, start_y, wall_idx) # 다 채우고 다음 진행을 위해 벽면 인덱스 갱신

    # print("===filled(1차)===")
    # for e in selected_arr:
    #     print(e)
    # print("======")
    # print("wall idx:", wall_idx)
    # ==== 유물 1차 획득 끝====
    # ==== 유물 연쇄 획득 시작====
    flag2 = True
    while flag2:
        max_value = get_max_val(selected_arr)
        if max_value < 3:
            flag2 = False
            break
        answer += max_value
        start_points = find_start_points(selected_arr)
            # print("===removed(연쇄)===")
            # for e in selected_arr:
            #     print(e)
            # print("======")
            # print(start_points)

        for start_x, start_y in start_points:
            wall_idx = fill(selected_arr, start_x, start_y, wall_idx) # 다 채우고 다음 진행을 위해 벽면 인덱스 갱신
        
            # print("===filled(연쇄)===")
            # for e in selected_arr:
            #     print(e)
            # print("======")
    # ==== 유물 연쇄 획득 끝====
    print(answer, end=" ")
    # 다음 진행을 위해 arr 갱신
    arr = [row[:] for row in selected_arr]
    turn += 1