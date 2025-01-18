import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

empty = []  # 빈 공간 좌표 저장
virus = []  # 바이러스(2)의 위치 저장
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈 공간과 바이러스 위치 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

# BFS 함수 (바이러스 확산)
def bfs(copy_arr):
    q = deque(virus)
    visited = [[False] * m for _ in range(n)]

    for vx, vy in virus:
        visited[vx][vy] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and copy_arr[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                copy_arr[nx][ny] = 2  # 감염 확산
                q.append((nx, ny))

# 3개의 벽을 세우는 모든 경우 탐색
for case in combinations(empty, 3):
    copy_arr = copy.deepcopy(arr)

    # 벽 설치
    for x, y in case:
        copy_arr[x][y] = 1

    # 바이러스 확산
    bfs(copy_arr)

    # 남은 안전 영역(0의 개수) 계산
    temp = sum(row.count(0) for row in copy_arr)
    ans = max(ans, temp)

print(ans)
