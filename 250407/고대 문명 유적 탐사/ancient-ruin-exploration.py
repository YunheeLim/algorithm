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
    path.add((x, y))
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
                cnt += dfs(grid, nx, ny, visited, path)
    return cnt

# 유물 가치 계산
def get_max_val(grid):
    max_val = 0
    visited = [[False] * 5 for _ in range(5)]
    total_route = [] # 모든 사라진 조각의 위치 저장
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                # 유물 삭제를 위해 기록 저장
                path = set()
                val = dfs(grid, i, j, visited, path)
                if val >= 3: # 유물 완성
                    max_val += val
                    total_route.extend(path)
                    # 유물 삭제
                    for x, y in path:
                        grid[x][y] = -1
    return max_val, total_route

# 유물 사라진 곳 숫자 채우기
def fill(grid, route, idx):
    route.sort(key=lambda x: (x[1], -x[0])) # 작은 열, 큰 행 순으로 정렬
    for i, j in route:
        grid[i][j] = nums[idx]
        idx += 1
    return idx # 마지막 조각까지 채우고 그 다음 벽면 숫자의 인덱스 반환

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

            # 3방향 회전
            rotated_tmp = []
            for degree in range(1, 4):
                rotated_tmp = rotate(tmp, degree)
                # 원래 배열에 합치기, 복사본으로
                copy_arr = [row[:] for row in arr]
                for rr in range(r, r + 3):
                    for cc in range(c, c + 3):
                        copy_arr[rr][cc] = rotated_tmp[rr - r][cc - c]
                get_max_value, total_route = get_max_val(copy_arr)
                if get_max_value >= max_value:
                    candidate.append([get_max_value, copy_arr, degree, c, r, total_route])


    candidate.sort(key=lambda x: (-x[0], x[2], x[3], x[4]))
    # 유물가치가 3개 이상 되는 경우가 없을 경우 탐사 중단
    if candidate[0][0] < 3:
        flag = False
        break
    selected_arr = candidate[0][1] # 유물가치가 최대가 되도록 회전한 배열
    # ==== 탐사 진행 끝 ====

    # ==== 유물 1차 획득 시작 ====
    answer += candidate[0][0] # 사라진 조각 개수
    total_route = candidate[0][5] # 사라진 조각들의 좌표

    wall_idx = fill(selected_arr, total_route, wall_idx) # 다 채우고 다음 진행을 위해 벽면 인덱스 갱신
    # ==== 유물 1차 획득 끝====

    # ==== 유물 연쇄 획득 시작====
    flag2 = True
    while flag2:
        max_value, total_route = get_max_val(selected_arr)
        if max_value < 3:
            flag2 = False
            break
        answer += max_value

        wall_idx = fill(selected_arr, total_route, wall_idx) # 다 채우고 다음 진행을 위해 벽면 인덱스 갱신
    # ==== 유물 연쇄 획득 끝====

    # 정답 출력
    print(answer, end=" ")

    # 다음 진행을 위해 arr 갱신
    arr = [row[:] for row in selected_arr]
    turn += 1