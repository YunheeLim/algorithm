import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

# 예외처리
if M == 0:
    print(0)
    exit()

arr = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r - 1][c - 1].append((s, d, z))  # 인덱스 0부터 시작

dx = [0, -1, 1, 0, 0]  # 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
dy = [0, 0, 0, 1, -1]

ans = 0

# 상어 이동
def move(x, y, s, d, z):
    if d in (1, 2):  # 위, 아래 방향 이동
        s %= (2 * (R - 1))  # 왕복 구간 최적화
    else:  # 왼쪽, 오른쪽 이동
        s %= (2 * (C - 1))

    for _ in range(s):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            x, y = nx, ny
        else:
            d = d + 1 if d % 2 else d - 1  # 방향 반전
            x, y = x + dx[d], y + dy[d]

    temp[x][y].append((s, d, z))


for cur in range(C):  # 낚시왕 이동
    # 1. 낚시: 가장 가까운 상어 잡기
    for i in range(R):
        if arr[i][cur]:
            s, d, z = arr[i][cur].pop()
            ans += z  # 잡은 상어 크기 추가
            break

    # 2. 상어 이동
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]:  # 해당 위치에 상어가 있으면
                s, d, z = arr[i][j][0]
                move(i, j, s, d, z)

    # 3. 같은 칸에 여러 마리의 상어가 있다면, 크기가 큰 것만 남김
    for i in range(R):
        for j in range(C):
            if len(temp[i][j]) > 1:
                temp[i][j].sort(key=lambda x: -x[2])  # 크기 기준 정렬
                temp[i][j] = [temp[i][j][0]]  # 가장 큰 상어만 남기기

    arr[:] = temp[:]  # 배열 덮어쓰기

print(ans)
