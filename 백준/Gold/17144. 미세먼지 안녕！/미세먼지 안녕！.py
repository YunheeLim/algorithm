import sys
import copy
input = sys.stdin.readline

# 입력 받기
r, c, t = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(r)]
dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]

# 공기청정기 위치 저장
purifier = []
for i in range(r):
    if dust[i][0] == -1:
        purifier.append(i)

# 공기청정기 작동 함수 (반시계, 시계 방향)
def air_purifier():
    # 위쪽 공기청정기 (반시계 방향)
    upper = purifier[0]
    for i in range(upper - 1, 0, -1):
        dust[i][0] = dust[i - 1][0]
    for i in range(c - 1):
        dust[0][i] = dust[0][i + 1]
    for i in range(upper):
        dust[i][c - 1] = dust[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
        dust[upper][i] = dust[upper][i - 1]
    dust[upper][1] = 0  # 공기청정기에서 나온 공기

    # 아래쪽 공기청정기 (시계 방향)
    lower = purifier[1]
    for i in range(lower + 1, r - 1):
        dust[i][0] = dust[i + 1][0]
    for i in range(c - 1):
        dust[r - 1][i] = dust[r - 1][i + 1]
    for i in range(r - 1, lower, -1):
        dust[i][c - 1] = dust[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        dust[lower][i] = dust[lower][i - 1]
    dust[lower][1] = 0  # 공기청정기에서 나온 공기

# 확산 함수
def spread_dust():
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if dust[i][j] > 0:
                cnt = 0
                amount = dust[i][j] // 5
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and dust[nx][ny] != -1:
                        temp[nx][ny] += amount
                        cnt += 1
                dust[i][j] -= amount * cnt

    # 확산된 먼지 더하기
    for i in range(r):
        for j in range(c):
            dust[i][j] += temp[i][j]

# `t`초 동안 실행
for _ in range(t):
    spread_dust()
    air_purifier()

# 결과 출력
answer = sum(sum(row) for row in dust) + 2  # 공기청정기(-1, -1) 보정
print(answer)
