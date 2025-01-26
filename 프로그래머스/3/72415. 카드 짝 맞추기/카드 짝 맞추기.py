from copy import deepcopy
from math import inf
from collections import deque

def get_key_count(board, cy, cx, ty, tx):
    dy = [1, 0, 0, -1]  # 아래, 오른쪽, 왼쪽, 위쪽
    dx = [0, 1, -1, 0]
    que = deque()
    que.append((cy, cx))
    visited = [[inf for _ in range(4)] for _ in range(4)]
    visited[cy][cx] = 0  # 시작 위치 방문 처리

    while que:
        y, x = que.popleft()
        if y == ty and x == tx:  # 목표 카드에 도달하면 이동 횟수 반환
            return visited[y][x]

        # 1. 상하좌우로 1칸씩 이동
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                que.append((ny, nx))

        # 2. CTRL + 방향키 이동 (장애물 또는 경계를 만날 때까지)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            while 0 <= ny + dy[i] < 4 and 0 <= nx + dx[i] < 4 and board[ny][nx] == 0:
                ny, nx = ny + dy[i], nx + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                que.append((ny, nx))
                
# 특정 숫자의 카드 위치 찾기
def get_coord_by_num(board, target):
    for i in range(4):
        for j in range(4):
            if board[i][j] == target:
                return i, j

answer = inf

# 모든 카드가 제거되었는지 확인
def is_end(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
    return True

# 모든 가능한 카드 제거 순서를 탐색하여 최소 이동 횟수 찾기
def dfs(board, r, c, ty1, tx1, cnt):
    global answer
    board = deepcopy(board)  # 현재 상태 복사 (원본 변경 방지)
    target_num = board[ty1][tx1]  # 현재 선택한 카드의 숫자

    # 1. 첫 번째 카드 선택
    cnt += get_key_count(board, r, c, ty1, tx1)
    board[ty1][tx1] = 0  # 카드 제거

    # 2. 두 번째 카드 선택 (같은 숫자의 카드 위치 찾기)
    ty2, tx2 = get_coord_by_num(board, target_num)
    cnt += get_key_count(board, ty1, tx1, ty2, tx2)
    board[ty2][tx2] = 0  # 카드 제거
    cnt += 2  # ENTER 키 입력 2회

    # 3. 모든 카드가 사라졌다면 결과 갱신
    if is_end(board):
        answer = min(answer, cnt)
    
    # 4. 남은 카드 탐색 & DFS 실행
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, ty2, tx2, i, j, cnt)

def solution(board, r, c):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, r, c, i, j, 0)

    return answer